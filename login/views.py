from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from login.stc_user_form import StcUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

def register(request):
    if request.method == 'POST':
        form = StcUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = StcUserCreationForm()
        
    context = {
        'form':form
    }

    return render(
        request,
        'register.html',
        context
    )

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
     
    return render(
        request,
        'login.html',
        None
    )

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')