from django.contrib.auth.models import User
from django.db import models
from blood.models import Blood
from doctors.models import Doctor


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='patients/images/')
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    blood_group = models.ForeignKey(Blood, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username


class PatientInstance(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    mrd_number = models.CharField(max_length=20, unique=True)
    diagnosed_case = models.TextField()
    medical_history = models.TextField()
    room_number = models.CharField(max_length=10, help_text='Either room number or ward number.')
    consulting_doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=False)
    pay_now = models.BooleanField(default=False)

    def __str__(self):
        return self.mrd_number


class BillCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Bill Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BillDetail(models.Model):
    patient_instance = models.ForeignKey(PatientInstance, on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=20)
    bill_category = models.ForeignKey(BillCategory, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    bill_image = models.ImageField(upload_to='bills/images/')

    def __str__(self):
        return self.bill_number


class Order(models.Model):
    token = models.CharField(max_length=256)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    email_address = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    billing_name = models.CharField(max_length=128)
    billing_address = models.CharField(max_length=128)
    billing_city = models.CharField(max_length=128)
    billing_postcode = models.CharField(max_length=6)
    billing_country = models.CharField(max_length=128)
    shipping_name = models.CharField(max_length=128)
    shipping_address = models.CharField(max_length=128)
    shipping_city = models.CharField(max_length=128)
    shipping_postcode = models.CharField(max_length=6)
    shipping_country = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.billing_name
