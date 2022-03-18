
from attr import field, fields
from django.forms import ModelForm
from django import forms
from .models import Customer, Leads, Csv , Task


class LeadForm(ModelForm):
    class Meta:
        model = Leads
        fields = '__all__'


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
