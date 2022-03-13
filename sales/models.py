from datetime import date
from django.db import models

# Create your models here.
class Leads(models.Model):
    lead_company = models.CharField(max_length=200)
    lead_name = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=10)
    lead_email = models.EmailField()
    address = models.CharField(max_length=500)
    requirement = models.CharField(max_length=1500)
    lead_managed = models.CharField(max_length=200)
    create_date = models.DateField(default=date.today)
    last_contacted = models.DateField(default=date.today)

    def __str__(self):
        return self.lead_name
