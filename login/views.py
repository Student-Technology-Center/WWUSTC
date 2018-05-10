from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

from .models import UserHiddenAttributes, UserOptions
from .helpers import send_user_confirmation_email, check_user_confirmation_key
from .forms import UserSignupForm, UserInformationForm, UserLoginForm, UserOptionsForm, EmailConfirmationForm

USER_MODEL = get_user_model()

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    context = { 
        'login_form' : UserLoginForm(),
        'information_form': UserInformationForm(),
        'registration_form': UserSignupForm()
    }

    return render(
        request,
        'login.html',
        context
    )

@login_required
def confirm_email(request, uuid=""):
    if request.user.userhiddenattributes.confirmed_account:
        return redirect('/')

    if uuid:
        if check_user_confirmation_key(uuid):
            return redirect('/')

    context = { 
        "confirmation_form" : EmailConfirmationForm()
    }

    return render(
        request,
        "confirm_email.html",
        context
    )

def reset_password(request):
    context = {}

    context['key'] = True
    context['wrong_key'] = False

    #Only enter this if the user attempts to enter their key
    if request.method == 'POST':
        if request.POST.get('password_reset', False):
            pw1 = request.POST.get('pw1', False)
            pw2 = request.POST.get('pw2', False)

            if not pw1 or not pw2 or pw1 != pw2:
                context['key'] = False
                context['pw_no_match'] = True

                return render(
                    request,
                    'password_reset.html',
                    context
                )

            request.user.set_password(pw2)
            request.user.save()
            return redirect('/')

        key = request.POST.get('key', False)
        attr = None

        try:
            attr = UserHiddenAttributes.objects.get(reset_key=key)
        except UserHiddenAttributes.DoesNotExist:
            context['wrong_key'] = True
            return render(
                request,
                'password_reset.html',
                context
            )

        if attr.reset_key == key:
            login(request, attr.user)
            context['key'] = False

    return render(
        request,
        'password_reset.html',
        context
    )

@login_required
def profile(request):
    context = {}

    if request.POST:
        form = UserOptionsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            m = UserOptions.objects.get(user=request.user)
            m.texting = f.texting
            m.email = f.email
            m.shift_name = f.shift_name
            m.phone_carrer = f.phone_carrier
            m.phone_number = f.phone_number
            m.save()
    else:
        options = UserOptions.objects.get(user=request.user)
        form = UserOptionsForm(initial={
            "shift_name" : options.shift_name,
            "phone_number" : options.phone_number,
            "phone_carrier" : options.phone_carrier,
            "texting" : options.texting,
            "email" : options.email
        })

    context['options'] = form

    return render(
        request,
        'profile.html',
        context
    )
