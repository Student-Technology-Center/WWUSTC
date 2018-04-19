from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

from .models import UserHiddenAttributes
from .helpers import send_user_confirmation_email, check_user_confirmation_key
from .forms import UserSignupForm, UserInformationForm, UserLoginForm, EmailConfirmationForm

USER_MODEL = get_user_model()

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    context = { 
        'login_form' : UserLoginForm(),
        'registration_form': UserInformationForm(),
        'signup_form': UserSignupForm()
    }

    return render(
        request,
        'login.html',
        context
    )

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

    context['users'] = get_user_model().objects.all()
    options = UserOptions.objects.get_or_create(user=request.user)

    if request.POST.get('update', False):
        context['form'] = UserOptionsForm(request.POST, initial={'phone_number': options[0].phone_number,'texting':options[0].texting, 'email':options[0].email, 
        'phone_carrier':options[0].phone_carrier})
    else:
        context['form'] = UserOptionsForm(None, initial={'phone_number': options[0].phone_number,'texting':options[0].texting, 'email':options[0].email, 
        'phone_carrier':options[0].phone_carrier})

    #short circuits 
    if request.POST.get('update', False) and context['form'].is_valid():
        options_form = context['form'].save(commit=False)
        options[0].phone_carrier = options_form.phone_carrier
        options[0].phone_number = options_form.phone_number
        options[0].texting = options_form.texting
        options[0].email = options_form.email
        options[0].save()

    if request.POST.get('motd_update', False):
        if request.user.is_superuser:
            settings.MOTD = request.POST.get('motd_text', 'Replacement')

    if request.POST.get('delete-users', False) and request.user.is_superuser:
        for i in request.POST.keys():
            if request.POST.get(i) == 'on':
                user = get_user_model().objects.get(pk=i.split('_')[1])
                user.delete()

    return render(
        request,
        'profile.html',
        context
    )
