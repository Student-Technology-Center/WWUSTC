from django.shortcuts import render
import requests

def index(request):

    context = {
        "user":request.user,
    }

    changelog = open('changelog.md')
    context['changelog'] = changelog.read()
    changelog.close()


    return render(
        request,
        "main_page.html",
        context
    )