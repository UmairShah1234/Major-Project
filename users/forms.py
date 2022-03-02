from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile
# X5j13$#eCM1cG@Kdc
class RegisterForm(UserCreationForm):  
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' ,'password2' ]
       

class ProfileForm(ModelForm):
    class Meta:
       model = Profile
       fields = '__all__'