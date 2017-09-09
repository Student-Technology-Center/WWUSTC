from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from random import randint

from utils.alerts.alerter import email

from login.models import UserHiddenAttributes

#TODO: Fix this throwing errors (works regardless)
@require_http_methods(['GET'])
def send_user_email(request):
    username = request.GET.get('user', False)

    if username == False:
        return JsonResponse({
            'status':'failure'
        })

    user = get_user_model().objects.get(username=username)
    _key = 0

    #because math is easier than string creation
    for i in range(0, 8):
        _key *= 10
        _key += randint(0, 9)

    key = str(_key)
    attr = UserHiddenAttributes.objects.get_or_create(user=user)

    attr[0].reset_key = key
    attr[0].save()

    msg = """It appears someone has requested to reset your password.\n
If you did not send this request, please ignore this message and contact\n
an admin ASAP. Your key is shown below.\n

Enter this key on the reset page:\n
    """

    msg = msg + " {}".format(key)
    email(user.email, '[STC] Password request key', msg)

    return JsonResponse({
        'status':'success'
    })

