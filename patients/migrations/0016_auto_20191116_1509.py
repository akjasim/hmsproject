# Generated by Django 2.2.6 on 2019-11-16 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_auto_20191116_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billdetail',
            name='user',
        ),
        migrations.AddField(
            model_name='billdetail',
            name='patient_instance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.PatientInstance'),
        ),
    ]
