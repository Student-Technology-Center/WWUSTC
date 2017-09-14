from django.shortcuts import render
import requests

def index(request):

    context = {
        "user":request.user,
    }

    quote = requests.get('https://talaikis.com/api/quotes/random/').json()

    return render(
        request,
        "main_page.html",
        context
    )