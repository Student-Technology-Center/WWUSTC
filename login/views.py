from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

from .models import UserHiddenAttributes, UserOptions
from .helpers import send_user_confirmation_email, check_user_confirmation_key
from .forms import UserSignupForm, UserInformationForm, UserLoginForm, UserOptionsForm, EmailConfirmationForm, PasswordResetRequest, PasswordReset

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

def reset_password(request):
    context = { 
        "request"   : PasswordResetRequest(),
        "reset"     : PasswordReset()
    }

    return render(
        request,
        "reset.html",
        context
    )

@login_required
def confirm_email(request, uuid=""):
    if request.user.userhiddenattributes.confirmed_account:
        return redirect('/')

    if not uuid:
        uuid = request.POST.get('uuid', "")
        uuid = uuid.replace(" ", "")

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
