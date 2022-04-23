import csv
import logging

from urllib import response
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomerForm, LeadForm, BulkForm, LeadmailForm, Task_Name_Form, TaskForm
from .models import Customer, LeadMail, Leads, Csv, Task,User


# Create your views here.


def leadform(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            # form.save()
            instance = form.save(commit=False)
            instance.user_name = request.user
            instance.save()
            print(request.user)
            # print(form.cleaned_data)

            return redirect('sales:viewleads')

    return render(request, 'sales/leadform.html', {'form': form})


def upload_file_view(request):
    form = BulkForm(request.POST or None, request.FILES or None)
    try:

        if form.is_valid():
            # for is taking all files instead of only csvs(bug)
            form.save()
            form = BulkForm()
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        # row = " ".join(row)
                        # # row = row.replace("", " ")
                        # row = row.split()
                        Leads.objects.create(
                            user_name=request.user,
                            lead_company=row[0],
                            lead_name=row[1],
                            phone_num=row[2],
                            lead_email=row[3],
                            address=row[4],
                            requirement=row[5],
                            lead_managed=row[6],

                        )

                        # print(row[4])
                        # print(type(row))
                obj.activated = True
                obj.save()
            return redirect('sales:viewleads')

    except Exception as e:
        logging.getLogger('error_logger').error(
            'Unable to upload file. ' + repr(e))
        messages.error(request, 'Unable to upload file. ' + repr(e))

    return render(request, 'sales/bulkleads.html', {'form': form})


def viewleads(request):

    if request.user.is_superuser:
        leads = Leads.objects.all()
    else:

        leads = Leads.objects.filter(user_name=request.user)
    context = {
        'leads': leads,

    }
    return render(request, 'sales/viewleads.html', context)


def deleteLead(request, id):

    leads = Leads.objects.get(pk=id)
    # print(leads)
    leads.delete()

    return redirect('sales:viewleads')


def updateLead(request, id):
    leads = Leads.objects.get(pk=id)
    form = LeadForm(instance=leads)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=leads)
        if form.is_valid():
            form.save()
            return redirect('sales:viewleads')
    return render(request, 'sales/updateleads.html', {'form': form})


def pushLead(request, id):
    lead = Leads.objects.get(pk=id)
    print(lead)
    Customer.objects.create(
        user_name=request.user,
        customer_company=lead.lead_company,
        customer_name=lead.lead_name,
        phone_num=lead.phone_num,
        lead_email=lead.lead_email,
        address=lead.address,
        requirement=lead.requirement,
        lead_managed=lead.lead_managed,

    )
    return redirect('sales:viewcustomers')


def viewcustomer(request):
    if request.user.is_superuser:
        customer = Customer.objects.all()
    else:
        customer = Customer.objects.filter(user_name=request.user)
    return render(request, 'sales/viewcustomers.html', {'customer': customer})


def deleteCustomer(request, id):
    customer = Customer.objects.get(pk=id)
    # print(leads)
    customer.delete()
    return redirect('sales:viewcustomers')


def updateCustomer(request, id):
    customer = Customer.objects.get(pk=id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('sales:viewcustomers')
    return render(request, 'sales/updatecustomers.html', {'form': form})


def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "added a new task")
    else:
        form = TaskForm()
    return render(request, "sales/createtask.html", {'form': form})


def viewtask(request):
    form = TaskForm()
    createTask(request)
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(managed_by=request.user)
    return render(request, 'sales/viewtask.html', {'tasks': tasks, 'form': form})

# displays the name of the lead


def leadTask(request, id):
    lead = Leads.objects.get(pk=id)
    print(lead.lead_name)
    form = Task_Name_Form()
    if request.method == 'POST':
        form = Task_Name_Form(request.POST)
        if form.is_valid():
            print('valid')
            instance = form.save(commit=False)
            instance.lead_name = lead
            instance.save()
            return redirect('sales:viewtask')

    context = {'form': form,
               'lead': lead}

    return render(request, 'sales/task.html', context)


# detailed view
def leadDetailedView(request,id):
    lead = Leads.objects.get(pk=id)
    print(lead.lead_company)
    return render(request,'sales/leaddetailedview.html',{'lead':lead})

def customerDetailedView(request,id):
    customer = Customer.objects.get(pk=id)
    print(customer.customer_company)
    return render(request,'sales/customerdetailedview.html',{'customer':customer})

# export leads data in csv 

def exportLeads(request):
    
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['company name','lead name','phone','email','address','requirement','lead managed by','create date','last contacted'])
    
    for data in Leads.objects.all().values_list('lead_company','lead_name','phone_num','lead_email','address','requirement','lead_managed','create_date','last_contacted'):
        writer.writerow(data)
    
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'
    
    return response

# export customer data in csv 
def exportCustomer(request):
    
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['company name','name','phone','email','address','requirement','customer managed by','create date','last contacted'])
    
    for data in Customer.objects.all().values_list('customer_company','customer_name','phone_num','lead_email','address','requirement','lead_managed','create_date','last_contacted'):
        writer.writerow(data)
    
    response['Content-Disposition'] = 'attachment; filename="customers.csv"'
    
    return response

# send mail to leads

def leadMail(request, id):
    form = LeadmailForm()
    lead = Leads.objects.get(pk=id)
    print(lead.lead_email)
    
    if request.method == 'POST':
        form = LeadmailForm(request.POST)
        if form.is_valid():
            subject = request.POST['subject']
            message = request.POST['message']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead.lead_email, ]

            send_mail(subject, message, email_from,recipient_list, fail_silently=False)

            LeadMail.objects.create(name=lead.lead_name,
            email=lead.lead_email,
            subject=subject,
            message=message
            )
            form.save()
            return redirect('sales:viewleads')
    
    context = {'lead':lead,
    'form':form}
        
    return render(request,'sales/mailform.html',context)

    # send mail to customers
def customerMail(request, id):
    form = LeadmailForm()
    customer = Customer.objects.get(pk=id)
    print(customer.lead_email)
    
    if request.method == 'POST':
        form = LeadmailForm(request.POST)
        if form.is_valid():
            subject = request.POST['subject']
            message = request.POST['message']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [customer.lead_email, ]

            send_mail(subject, message, email_from,recipient_list, fail_silently=False)

            LeadMail.objects.create(name=customer.customer_name,
            email=customer.lead_email,
            subject=subject,
            message=message
            )
            form.save()
            return redirect('sales:viewcustomers')
    
    context = {'customer':customer,
    'form':form}
        
    return render(request,'sales/mailform.html',context)