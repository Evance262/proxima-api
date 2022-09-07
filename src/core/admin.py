from django.contrib import admin
from .models import BankAccount, CreditCard

admin.site.register(BankAccount)
admin.site.register(CreditCard)
