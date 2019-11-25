import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import View

from .models import UserProfile, BillDetail, PatientInstance, Order


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'patients/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = PatientInstance.objects.all().filter(patient=self.request.user).order_by('-pk')
        return context


class CaseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = PatientInstance
    template_name = 'patients/case-detail.html'

    def test_func(self):
        patient_object = PatientInstance.objects.get(pk=self.kwargs.get('pk'))
        return patient_object.patient.pk == self.request.user.pk

    def get_context_data(self, **kwargs):
        """
            Commented lines are related to payment gateway! Payment gateway is disabled.
        """
        context = super().get_context_data(**kwargs)
        total_amount = 0
        # description = 'Bill Payment'
        bills = BillDetail.objects.all().filter(patient_instance=self.object.pk)
        for bill in bills:
            total_amount += bill.amount
        context['bills'] = bills
        context['bill_amount'] = total_amount
        # context['stripe_total'] = total_amount*100
        # self.request.session['total'] = str(total_amount)
        # context['data_description'] = description
        # self.request.session['description'] = description
        # context['data_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


"""
    PaymentView class represents payment gateway. It is currently disabled.
"""
# class PaymentView(View):
#     def post(self, request, *args, **kwargs):
#         stripe_total = int(self.request.session.get('total') * 100)
#         print(stripe_total)
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         try:
#             stripe_token = request.POST.get('stripeToken')
#             stripe_email = request.POST.get('stripeEmail')
#             stripe_billing_name = request.POST.get('stripeBillingName')
#             stripe_billing_address = request.POST.get('stripeBillingAddressLine1')
#             stripe_billing_city = request.POST.get('stripeBillingAddressCity')
#             stripe_billing_postcode = request.POST.get('stripeBillingAddressZip')
#             stripe_billing_country = request.POST.get('stripeBillingAddressCountryCode')
#             stripe_shipping_name = request.POST.get('stripeShippingName')
#             stripe_shipping_address = request.POST.get('stripeShippingAddressLine1')
#             stripe_shipping_city = request.POST.get('stripeShippingAddressCity')
#             stripe_shipping_postcode = request.POST.get('stripeShippingAddressZip')
#             stripe_shipping_country = request.POST.get('stripeShippingAddressCountryCode')
#
#             new_customer = stripe.Customer.create(
#                 source=stripe_token,
#                 email=stripe_email
#             )
#             stripe.Charge.create(
#                 customer=new_customer.id,
#                 amount=stripe_total,
#                 description=self.request.session.get('description'),
#                 currency='inr'
#             )
#             ''' Create new order '''
#             try:
#                 new_order = Order.objects.create(
#                     token=stripe_token,
#                     total=request.session.get('total'),
#                     email_address=stripe_email,
#                     billing_name=stripe_billing_name,
#                     billing_address=stripe_billing_address,
#                     billing_city=stripe_billing_city,
#                     billing_postcode=stripe_billing_postcode,
#                     billing_country=stripe_billing_country,
#                     shipping_name=stripe_shipping_name,
#                     shipping_address=stripe_shipping_address,
#                     shipping_city=stripe_shipping_city,
#                     shipping_postcode=stripe_shipping_postcode,
#                     shipping_country=stripe_shipping_country,
#                     user=request.user
#                 )
#                 current_patient = PatientInstance.objects.get(user=request.user)
#                 current_patient.pay_now = False
#                 current_patient.save()
#                 messages.success(request, f'Thank you for placing online. Your discharge ID is {new_order.id}.')
#                 return redirect('order-detail', pk=new_order.id)
#             except ObjectDoesNotExist:
#                 raise Http404
#         except stripe.error.CardError as e:
#             raise Http404
