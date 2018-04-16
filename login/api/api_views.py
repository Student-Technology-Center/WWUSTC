from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect
from django.http import JsonResponse

from random import randint

from login.models import UserHiddenAttributes
from ..forms import UserLoginForm, UserSignupForm, UserInformationForm

USER_MODEL = get_user_model()

@require_http_methods(['POST'])
def register(request):

    register = UserSignupForm(request.POST)
    info = UserInformationForm(request.POST)

    if register.is_valid() and info.is_valid():
        username = register.cleaned_data.get('username')
        password = register.cleaned_data.get('password1')

        USER_MODEL.objects.create_user(first_name=register.cleaned_data.get('first_name'),
                                       last_name=register.cleaned_data.get('last_name'),
                                       email=register.cleaned_data.get('email'),
                                       username=username,
                                       password=password)

        user = authenticate(username=username, password=password)

        if user is not None:
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
        test = USER_MODEL.objects.get(username=username)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "success": {"Account":"Logged in."}    
            })
        else:
            return JsonResponse({
                "failed": {"Error":"User not found with that information"}
            })
    else:
        return JsonResponse({
            "failed": info.errors
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
def api_confirm_email(request, uuid):
    print(uuid)
    return JsonResponse({
        "failed": {"Because": "Idiot"}
    })

