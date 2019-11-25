from django.db import models


class Department(models.Model):
    class Meta:
        verbose_name_plural = 'Departments'

    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    category = models.ForeignKey(Department, on_delete=models.CASCADE)
    max_token = models.IntegerField(default=100)

    def __str__(self):
        return self.name
