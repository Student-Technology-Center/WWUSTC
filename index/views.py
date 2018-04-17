from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.conf import settings
from login.decorators import user_is_email_confirmed

@login_required
@user_is_email_confirmed
def index(request):
    '''
    Below is where we define who will become an admin, as the index will check.
    '''
    context = { }

    print(request.user.groups)

    return render(
        request,
        "main_page.html",
        context
    )