from django.contrib import admin
from .models import Customer, Leads, Csv  , Task

# Register your models here.

admin.site.register(Leads)
admin.site.register(Csv)
admin.site.register(Customer)
admin.site.register(Task)
