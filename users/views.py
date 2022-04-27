
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from sales.models import Task,Team


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

from sales.models import Leads , Customer
@login_required
def dashboard(request):


    datefields = Leads.objects.all()
    count_leads = Leads.objects.filter(user_name=request.user).count()
    count_leads_super = Leads.objects.count()
    count_tasks = Task.objects.filter(created_by=request.user).count()
    count_tasks_super = Task.objects.count()
    count_cust = Customer.objects.filter(user_name=request.user).count()
    count_cust_super = Customer.objects.count()
    count_team = Team.objects.filter(created_by=request.user).count()
    print(count_leads,count_tasks,count_cust,count_team)
    user_names = []
    dates = []
    count_date = []
    lead_count = []
    temp = []
    
    
    for date in datefields:
        if date.create_date not in dates:
            dates.append(date.create_date)
    for date in datefields:
        temp.append(date.create_date) 
    for x in dates:
        count = temp.count(x)
        count_date.append(count)

    if request.user.is_superuser:
        leads = Leads.objects.all()
        # count_leads_super = Leads.objects.count()
        temp1 = []
        
        for name in leads:
            if name.lead_managed not in user_names:
                user_names.append(name.lead_managed)
        for lead in leads:
            temp1.append(lead.lead_managed)
        for x in user_names:
            count = temp1.count(x)
            lead_count.append(count)
        
    context = {
        'datefields' : datefields , 
        'dates' : dates , 
        'count_date' : count_date , 
        'user_names' : user_names , 
        'lead_count' : lead_count , 
        'count_leads':count_leads,
        'count_tasks':count_tasks,
        'count_cust':count_cust,
        'count_team':count_team,
        'count_leads_super':count_leads_super,
        'count_tasks_super':count_tasks_super,
        'count_cust_super':count_cust_super

    }
    return render(request, 'users/dashboard.html' , context)
