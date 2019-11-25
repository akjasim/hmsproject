from django.urls import path

from patients import views
from .views import HomeView, CaseDetailView

app_name = 'patients'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cases/<int:pk>/', CaseDetailView.as_view(), name='case-detail'),
    # path('payments/', views.PaymentView.as_view(), name='payments')
]
