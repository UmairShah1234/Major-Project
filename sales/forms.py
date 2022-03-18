
from django.forms import ModelForm
from django import forms
from .models import Customer, Leads, Csv


class LeadForm(ModelForm):
    class Meta:
        model = Leads
        fields = ('lead_company', 'lead_name', 'phone_num', 'lead_email', 'address',
                  'requirement', 'lead_managed', 'create_date', 'last_contacted')


class BulkForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
