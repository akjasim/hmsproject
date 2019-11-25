from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as g
from appointments.models import Appointment
from doctors.models import Department, Doctor
from datetime import date
# INSERT INTO model ()asf


class HomeView(SuccessMessageMixin, g.CreateView):
    model = Appointment
    fields = ('name', 'phone_number', 'doctor', 'date')
    extra_context = {'department_list': Department.objects.all()}
    template_name = 'pages/home.html'
    success_url = reverse_lazy('pages:home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('patients:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        cd = form.cleaned_data
        if cd.get('date') < date.today():
            messages.error(self.request, 'Please select correct date!')
            return redirect('pages:home')
        latest_token_object = Appointment.objects.filter(doctor=cd.get('doctor'), date=cd.get('date')).last()
        # print(latest_token_object)
        if latest_token_object:
            if latest_token_object.token_number == cd.get('doctor').max_token:
                messages.error(self.request, 'Token full. Please consider next days!')
                return redirect('pages:home')
        if latest_token_object is None:
            form.instance.token_number = 1
        else:
            form.instance.token_number = latest_token_object.token_number + 1
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return f'Thank you for your appointment. Your token number is {self.object.token_number}.'
