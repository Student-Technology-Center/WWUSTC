from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.conf import settings

import requests

@login_required
def index(request):
    '''
    Below is where we define who will become an admin, as the index will check.
    '''
    context = { }

    return render(
        request,
        "main_page.html",
        context
    )