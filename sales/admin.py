from django.contrib import admin
from .models import Customer, LeadMail, Leads, Csv , Task, Team
# Register your models here.

admin.site.register(Leads)
admin.site.register(Csv)
admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(LeadMail)
admin.site.register(Team)
