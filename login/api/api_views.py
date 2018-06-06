from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.http import JsonResponse

from random import randint

from ..models import UserHiddenAttributes
from ..helpers import send_user_confirmation_email
from ..forms import UserLoginForm, UserSignupForm, UserInformationForm, PasswordResetRequest

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

@require_http_methods(['GET'])
def reset_password(request):
    reset_request = PasswordResetRequest(request.GET)
    
    if reset_request.is_valid():
        return JsonResponse({
            "success" : "Sent to {}".format(request.GET.get("email"))
        })

    return JsonResponse({
        "failed" : "No account associated with {}".format(request.GET.get("email", ""))
    })


