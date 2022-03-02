from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email_id = models.EmailField()
    profile_image = models.ImageField(default='profile_pic.jpg' , upload_to='profile_picture')
    birth_date = models.DateField(default=None)
    password1 = models.CharField(max_length=10 , default='')
    password2 = models.CharField(max_length=10 , default='')

    def __str__(self):
        return self.username