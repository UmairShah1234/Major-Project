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
    path('deletecustomers/<int:id>/',
         views.deleteCustomer, name='deletecustomers'),
    path('updatecustomer/<int:id>', views.updateCustomer, name='updatecustomer'),
    path('viewtask/', views.viewtask, name='viewtask'),
    path('createtask/', views.createTask, name='createatask'),
    path('task/<int:id>/', views.leadTask, name='task'),
    path('leaddetailedview/<int:id>',views.leadDetailedView,name='leadDetailedView'),
    path('exportleads',views.exportLeads,name='exportLeads'),
    path('exportcustomer',views.exportCustomer,name='exportCustomer')
]
