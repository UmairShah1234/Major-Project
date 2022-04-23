from unicodedata import name
from django.urls import include, path
from . import views
app_name = 'salesanalysis'
urlpatterns = [
   path('analysis/',views.analysis , name='analysis'),
   path('customeranalysis/',views.customeranalysis , name='customeranalysis'),
   path('useranalysis/',views.useranalysis , name='useranalysis'),
]