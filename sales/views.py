import csv
import logging


from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CustomerForm, LeadForm, BulkForm
from .models import Customer, Leads, Csv


# Create your views here.


def leadform(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('sales:viewleads')
    return render(request, 'sales/leadform.html', {'form': form})


def upload_file_view(request):
    form = BulkForm(request.POST or None, request.FILES or None)
    try:

        if form.is_valid():
            # for is taking all files instead of csvs(bug)
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

    except Exception as e:
        logging.getLogger('error_logger').error(
            'Unable to upload file. ' + repr(e))
        messages.error(request, 'Unable to upload file. ' + repr(e))

    return render(request, 'sales/bulkleads.html', {'form': form})


def viewleads(request):
    leads = Leads.objects.all()
    return render(request, 'sales/viewleads.html', {'leads': leads})


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
        if form.is_valid:
            form.save()
            return redirect('sales:viewleads')
    return render(request, 'sales/updateleads.html', {'form': form})


def pushLead(request, id):
    lead = Leads.objects.get(pk=id)
    print(lead)
    Customer.objects.create(
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
    customer = Customer.objects.all()
    return render(request, 'sales/viewcustomers.html', {'customer': customer})


def deleteLead(request, id):

    customer = Customer.objects.get(pk=id)
    # print(leads)
    customer.delete()

    return redirect('sales:viewcustomers')


def updateCustomer(request, id):
    customer = Customer.objects.get(pk=id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid:
            form.save()
            return redirect('sales:viewcustomers')
    return render(request, 'sales/updatecustomers.html', {'form': form})
