# Generated by Django 2.2.6 on 2019-11-10 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_auto_20191109_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinstance',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
