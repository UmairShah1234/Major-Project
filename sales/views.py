from django.shortcuts import render
from .forms import LeadForm

# Create your views here.
def leadform(request):
    form = LeadForm()
    return render(request , 'sales/leadform.html' , {'form':form})
