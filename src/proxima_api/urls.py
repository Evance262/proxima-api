"""proxima_api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from core.views import CreditCardView, BankAccountView

urlpatterns = [
    path('api-auth/',
         include('rest_framework.urls',)),
    path('admin/', admin.site.urls),
    path('credit_card/', CreditCardView.as_view(), name='credit_card'),
    path('bank_account/', BankAccountView.as_view(), name='bank_account')
]
