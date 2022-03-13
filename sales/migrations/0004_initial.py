# Generated by Django 4.0.2 on 2022-03-12 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0003_delete_leads'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_company', models.CharField(max_length=200)),
                ('lead_name', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=10)),
                ('lead_email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('requirement', models.CharField(max_length=1500)),
                ('lead_managed', models.CharField(max_length=200)),
                ('create_date', models.DateField(default=datetime.date.today)),
                ('last_contacted', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]