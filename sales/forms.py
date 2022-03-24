
from pyexpat import model
from attr import field, fields
from django.forms import ModelForm
from django import forms
from .models import Customer, Leads, Csv, Task


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


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

# displays the name of the lead


class Task_Name_Form(ModelForm):
    class Meta:
        model = Task
        fields = ('task_details', 'created_by', 'managed_by', 'managed_date')
