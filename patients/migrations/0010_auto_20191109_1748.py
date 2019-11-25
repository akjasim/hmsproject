# Generated by Django 2.2.6 on 2019-11-09 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_department_icon'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blood', '0001_initial'),
        ('patients', '0009_patient_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrd_number', models.CharField(max_length=20)),
                ('diagnosed_case', models.TextField()),
                ('medical_history', models.TextField()),
                ('room_number', models.CharField(help_text='Either room number or ward number.', max_length=10)),
                ('active', models.BooleanField(default=False)),
                ('consulting_doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='patients/images/')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=10)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blood.Blood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.AddField(
            model_name='patientinstance',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Profile'),
        ),
    ]
