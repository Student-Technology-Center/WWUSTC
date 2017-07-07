from django.shortcuts import render

def index(request):

    context = {
        "user":request.user,
    }

    return render(
        request,
        "main_page.html",
        context
    )