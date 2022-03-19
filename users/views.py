import re
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, "users/base.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} , account created')
            return redirect('users:dashboard')
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {'form': form})


@login_required
def profile_page(request):
    return render(request, 'users/profile_page.html')


@login_required
def profile_form(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:base')
    else:
        form = ProfileForm()
    return render(request, "users/profileForm.html", {'form': form})


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')
