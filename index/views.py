from django.shortcuts import render
import requests

def index(request):

    context = {
        "user":request.user,
    }

    context['issues'] = requests.get('https://api.github.com/repos/Student-Technology-Center/WWUSTC/issues').json()

    return render(
        request,
        "main_page.html",
        context
    )