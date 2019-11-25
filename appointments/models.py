from django.db import models

from doctors.models import Department, Doctor


class Appointment(models.Model):
    name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=10)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    token_number = models.IntegerField()
    date = models.DateField()
    booked_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
