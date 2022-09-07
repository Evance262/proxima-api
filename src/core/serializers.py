from rest_framework import serializers
from .models import BankAccount, CreditCard

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = (
            'user',
            'account_type',
            'routing_num',
            'account_num',
        )


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = (
            'user',
            'card_num',
            'card_type',
            'exp_date',
            'secu_code',
            'billing_address',
        )