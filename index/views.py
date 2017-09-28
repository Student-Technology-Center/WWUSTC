from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.conf import settings

import requests

def index(request):

    '''
    Below is where we define who will become an admin, as the index will check.
    '''

    user_model = get_user_model()

    for name in settings.ADMIN_LIST:

        try:
            user = user_model.objects.get(username=name)
        except:
            break

        user.is_superuser = True
        user.save()

    context = {
        "user":request.user,
        "creating_shifts":settings.CREATING_SHIFTS,
        "motd":settings.MOTD
    }

    return render(
        request,
        "main_page.html",
        context
    )