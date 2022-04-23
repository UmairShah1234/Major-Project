from django.shortcuts import render
from sales.models import Leads , Customer
# Create your views here.

def analysis(request):
    datefields = Leads.objects.all()
    dates = []
    count_date = []
    temp = []
    
    for date in datefields:
        if date.create_date not in dates:
            dates.append(date.create_date)
    for date in datefields:
        temp.append(date.create_date) 
    for x in dates:
        count = temp.count(x)
        count_date.append(count)
    context = {
        'datefields' : datefields , 
        'dates' : dates , 
        'count_date' : count_date , 
    }
   
    return render(request, 'salesanalysis/analysis.html' , context)

def customeranalysis(request):
    customerfields = Customer.objects.all()
    dates = []
    count_date = []
    temp = []
    for date in customerfields:
        if date.create_date not in dates:
            dates.append(date.create_date)
    for date in customerfields:
        temp.append(date.create_date) 
    for x in dates:
        count = temp.count(x)
        count_date.append(count)
    context = {
        
        'dates' : dates , 
        'count_date' : count_date , 
    }
    return render(request  , 'salesanalysis/customeranalysis.html' , context)

def useranalysis(request):
    if request.user.is_superuser:
        leads = Leads.objects.all()
        user_names = []
        temp = []
        lead_count = []
        for name in leads:
            if name.lead_managed not in user_names:
                user_names.append(name.lead_managed)
        for lead in leads:
            temp.append(lead.lead_managed)
        for x in user_names:
            count = temp.count(x)
            lead_count.append(count)
        context = {
            'user_names' : user_names , 
            'lead_count' : lead_count , 
        }
        
    return render(request , 'salesanalysis/useranalysis.html' , context)

