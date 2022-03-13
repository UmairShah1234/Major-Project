from django.forms import ModelForm
from .models import Leads

class LeadForm(ModelForm):
    class Meta:
        model = Leads
        fields ='__all__'
