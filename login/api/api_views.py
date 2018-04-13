from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect
from django.http import JsonResponse
import json

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
        password = register.cleaned_data.get('password')
        first = register.cleaned_data.get('first_name')
        last = register.cleaned_data.get('last_name')
        email = register.cleaned_data.get('email')

        USER_MODEL.objects.create_user(username=username,
                                       password=password,
                                       first_name=first,
                                       last_name=last,
                                       email=email)
    else:
        print("Errors: {} | {}".format(register.errors, info.errors))

    return JsonResponse({
        "failed": {"System":"Control should not reach here, please report this."}
    })

@require_http_methods(['POST'])
def api_login(request):

    info = UserLoginForm(request.POST)

    if info.is_valid():
        username = info.cleaned_data['login']
        password = info.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "success": {"Account":"Logged in."}    
            })
        else:
            return JsonResponse({
                "failed": {"Account":"User does not exist"}
            })
    else:
        return JsonResponse({
            "failed": info.errors
        })            

    return JsonResponse({
        "failed": {"System":"Control should not reach here, please report this."}
    })

@require_http_methods(['GET'])
def api_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({
            "success" : {"User":"Logged user out"}    
        })
    else:
        return JsonResponse({
            "failed" : {"User":"Not logged in"}
        })


