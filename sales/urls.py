from django.urls import  path
from . import views
app_name= 'sales'
urlpatterns = [
    
    path('leadform/' , views.leadform, name='leadform')
]