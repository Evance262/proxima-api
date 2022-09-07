from django.conf import settings
from django.db import models

ACCOUNT_TYPE_CHOICES = [
    ('Checking', 'Checking'),
    ('Savings', 'Savings',)
]

CARD_TYPE_CHOICES = [
    ('Visa', 'Visa'),
    ('Mastercard', 'Mastercard')
]

class BankAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)
    account_type = models.CharField(max_length=250, choices=ACCOUNT_TYPE_CHOICES)
    routing_num = models.IntegerField(help_text="Debit or credit",
                                      verbose_name="Routing number")
    account_num = models.IntegerField(help_text="Account number",
                                      verbose_name="Account number")

    def __str__(self):
        return self.account_type

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Bank account'
        verbose_name_plural = 'Bank accounts'


class CreditCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.CASCADE)
    card_num = models.IntegerField(help_text="Debit or credit",
                                   verbose_name="card number")
    card_type = models.CharField(max_length=250, choices=CARD_TYPE_CHOICES)
    exp_date = models.DateTimeField(blank=False,
                                    verbose_name='expiration date')
    secu_code  = models.IntegerField(blank=False,
                                     verbose_name='Security code')
    billing_address = models.CharField(max_length=1520)

    def __str__(self):
        return self.card_type

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Credit card'
        verbose_name_plural = 'Credit cards'