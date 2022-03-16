# Generated by Django 4.0.2 on 2022-03-16 13:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0006_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_name', models.CharField(max_length=200)),
                ('task_details', models.CharField(max_length=500)),
                ('managed_by', models.CharField(max_length=200)),
                ('managed_date', models.DateField(default=datetime.date.today)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
