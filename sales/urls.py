from django.urls import path
from . import views
app_name = 'sales'
urlpatterns = [

    path('leadform/', views.leadform, name='leadform'),
    path('bulkleads/', views.upload_file_view, name='bulkleads'),
    path('viewleads/', views.viewleads, name='viewleads'),
    path('delete_lead/<int:id>/', views.deleteLead, name='delete_lead'),
    path('updatelead/<int:id>', views.updateLead, name='updatelead'),
    path('pushlead/<int:id>', views.pushLead, name='pushlead'),
    path('viewcustomers/', views.viewcustomer, name='viewcustomers'),
    path('deletecustomers/<int:id>/', views.deleteLead, name='deletecustomers'),
    path('updatecustomer/<int:id>', views.updateCustomer, name='updatecustomer'),
    path('createtask/',views.createTask,name='createtask'),
]
