from datetime import date
import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.


class Leads(models.Model):
    user_name = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
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


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"File id: {self.id}"


class Customer(models.Model):
    user_name = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    customer_company = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=10)
    lead_email = models.EmailField()
    address = models.CharField(max_length=500)
    requirement = models.CharField(max_length=1500)
    lead_managed = models.CharField(max_length=200)
    create_date = models.DateField(default=date.today)
    last_contacted = models.DateField(default=date.today)

    def __str__(self):
        return self.customer_name


class Task(models.Model):

    lead_name = models.CharField(max_length=200)
    task_details = models.CharField(max_length=500)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lead_user", null=True)
    managed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    managed_date = models.DateField(default=date.today)

    def __str__(self):
        return self.lead_name

# ,widgets=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Details here'})

class LeadMail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='creator',null=True)
    team_manager = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='manager')
    member1 = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='member1')
    member2 = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='member2')

    def __str__(self):
        return self.team_name
    