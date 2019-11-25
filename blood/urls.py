from django.urls import path
from django.views.generic import ListView
from .models import Blood

app_name = 'blood'

urlpatterns = [
    path('', ListView.as_view(model=Blood), name='home'),
]
