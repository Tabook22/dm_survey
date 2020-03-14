from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout as django_logout
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# def login(request):
#     pass
@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError(
                    'Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'sr_user/register.html', {'form': form})


@login_required
def logout(request):
    # Your view logout is overriding the namespace of built-in logout function. Define an alias for django.contrib.auth.login function using as keyword.
    django_logout(request)
    return HttpResponseRedirect('/')


@login_required
def sr_control(request):
    return render(request, "sr_user/sr_control.html")
