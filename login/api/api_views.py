from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils import timezone

import random, string # Used to generate the password reset key

from ..models import UserHiddenAttributes
from ..helpers import send_user_confirmation_email, send_password_reset_email, check_password_reset_token
from ..forms import UserLoginForm, UserSignupForm, UserInformationForm, PasswordResetRequest, PasswordResetVerify, NewPasswordForm

USER_MODEL = get_user_model()

@require_http_methods(['POST'])
def register(request):

    register = UserSignupForm(request.POST)
    info = UserInformationForm(request.POST)

    if register.is_valid() and info.is_valid():
        username = register.cleaned_data.get('username')
        password = register.cleaned_data.get('password1')
        email = register.cleaned_data.get('email')
        employee = info.cleaned_data.get('employee_type')

        USER_MODEL.objects.create_user(first_name=register.cleaned_data.get('first_name'),
                                       last_name=register.cleaned_data.get('last_name'),
                                       email=email,
                                       username=username,
                                       password=password)

        user = authenticate(username=username, password=password)

        if user is not None:
            send_user_confirmation_email(request, user)
            grp, created = Group.objects.get_or_create(name=employee)
            grp.user_set.add(user)
            grp.save()

            login(request, user)
            return JsonResponse({
                "success": {"Account":"Created"}    
            })
    else:
        return JsonResponse({
            "failed" : register.errors
        }) 

    return JsonResponse({
            "failed": {"Account":"Failed to create user"}
    })

@require_http_methods(['POST'])
def api_login(request):
    info = UserLoginForm(request.POST)

    if info.is_valid():
        username = info.cleaned_data['login']
        password = info.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "success": {"Account":"Logged in."}    
            })
        else:
            return JsonResponse({
                "failed": {"Error":"User doesn't exist or username/password incorrect."}
            })
    else:
        return JsonResponse({
            "failed": info.errors.as_json()
        })            

    return JsonResponse({
        "failed": {"System":"Control should not reach here, please report this."}
    })

@require_http_methods(['GET'])
@login_required
def api_logout(request):
    logout(request)
    return JsonResponse({
        "success" : {"User":"Logged user out"}    
    })

@require_http_methods(['GET'])
@login_required
def send_email(request):
    send_user_confirmation_email(request, request.user)
    return JsonResponse({
        "success" : {"Email":"Sent!"}    
    })


# Generates a new request token and timeout for the account with the given email 
@require_http_methods(['GET'])
def reset_request(request):
    reset_request = PasswordResetRequest(request.GET)
    
    if reset_request.is_valid():

        reset_key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))

        user = USER_MODEL.objects.get(email=request.GET.get('email'))
        user_attributes = UserHiddenAttributes.objects.get(user=user)
        user_attributes.reset_key = reset_key
        user_attributes.reset_request_time = timezone.now()
        user_attributes.save()
        
        send_password_reset_email(request, user)

        return JsonResponse({
            "success" : "Sent to {}".format(request.GET.get("email"))
        })

    return JsonResponse({
        "failed" : "No account associated with {}".format(user.email)
    })

# Verify that the token is valid, either by the user clicking on the 
# emailed link or by entering the token manually
@require_http_methods(['GET'])
def reset_verify(request):
    reset_verify = PasswordResetVerify(request.GET)

    if reset_verify.is_valid():
        url = request.get_raw_uri().replace(request.get_full_path(), "") + "/user/reset/" + reset_verify.cleaned_data.get("key")
        return JsonResponse({
            "success" : "Password ready to be reset",
            "url"     : url
        })

    return JsonResponse({
        "failed" : "Invalid password reset token"
    })

@require_http_methods(['POST'])
def set_password(request):
    new_password = NewPasswordForm(request.POST)

    if new_password.is_valid():

        token = new_password.cleaned_data.get("token")
        attributes = UserHiddenAttributes.objects.get(reset_key=token)

        attributes.reset_key = None
        attributes.reset_request_time = None
        attributes.save()

        user = attributes.user
        user.set_password(new_password.cleaned_data.get("new_pass"))
        user.save()
        
        return JsonResponse({
            "success" : "Password reset, you may now login"    
        })

    return JsonResponse({
        "failed" : "Passwords don't match or your token expired"
    })



