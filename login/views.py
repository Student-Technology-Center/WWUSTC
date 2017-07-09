from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponseRedirect
from login.stc_user_form import StcUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

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
                return HttpResponseRedirect('/user/login/')
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
            return HttpResponseRedirect('/')
     
    return render(
        request,
        'login.html',
        None
    )

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')