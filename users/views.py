

from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.


def index(request):
    return render(request, "users/base.html")

# send_email


def send_email(request,username, email):
    domain = get_current_site(request)
    print(domain)
    subject = 'Verify Email '
    message = f'Hi {username}, Welcom To Crm App. Please Click The link to register http://{domain}/activate/{username} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    

    send_mail(subject, message, email_from,
              recipient_list, fail_silently=False)


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            instance = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # password = form.cleaned_data('password2')
            # user = User.objects.filter(username=username)
            
            instance.is_active = False
            instance.save()
            
            
            messages.success(request, f'Welcome {username} , account created Successfully, to verify your account please check your email')
            
            print(username, email)

            send_email(request=request ,username=username,email=email)

            return redirect('users:register')
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {'form': form})

def activate(request,username):
    obj = User.objects.get(username=username)
    obj.is_active = True
    obj.save()
    messages.success(request, f'Welcome {username} , account verified Successfully, You can Now Login')
    return redirect('users:login')

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
