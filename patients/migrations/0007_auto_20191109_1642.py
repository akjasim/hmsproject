# Generated by Django 2.2.6 on 2019-11-09 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20191109_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='consulting_doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.Doctor'),
        ),
    ]
