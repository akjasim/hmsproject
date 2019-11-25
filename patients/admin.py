from django.contrib import admin
from patients.models import UserProfile, PatientInstance, BillCategory, BillDetail

admin.site.register(UserProfile)
admin.site.register(PatientInstance)
admin.site.register(BillCategory)
admin.site.register(BillDetail)
