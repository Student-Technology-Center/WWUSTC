from django.shortcuts import render
from django.contrib.auth import get_user_model
import requests

def index(request):

    '''
    Below is where we define who will become an admin, as the index will check.
    '''

    admin_usernames = [
        'brintnc',
        'test' #TODO: REMOVE THIS <---
    ]

    user_model = get_user_model()

    for name in admin_usernames:
        try:
            user = user_model.objects.get(username=name)
        except:
            break
        user.is_superuser = True
        user.save()

    context = {
        "user":request.user,
    }

    return render(
        request,
        "main_page.html",
        context
    )