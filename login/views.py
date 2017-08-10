from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from login.stc_user_form import StcUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from login.models import UserOptions, UserOptionsForm

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

                return redirect('/')
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
            return redirect('/')
     
    return render(
        request,
        'login.html',
        None
    )

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    context = { }

    options = UserOptions.objects.get_or_create(user=request.user)

    context['form'] = UserOptionsForm(request.POST or None, initial={'phone_number': options[0].phone_number,'texting':options[0].texting, 'email':options[0].email})

    if context['form'].is_valid() and request.method == 'POST':
        options_form = context['form'].save(commit=False)
        options[0].phone_number = options_form.phone_number
        options[0].texting = options_form.texting
        options[0].email = options_form.email
        options[0].save()

    return render(
        request,
        'profile.html',
        context
    )