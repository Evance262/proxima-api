from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from datetime import date
from django_countries.fields import CountryField
from phone_field import PhoneField


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female',)
]

class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name="Date of Birth", null=True, blank=True)
    gender      = models.CharField(verbose_name="Gender", null=True, max_length=50, choices=GENDER_CHOICES, default="")
    phone_no    = PhoneField(blank=True, help_text="Contact phone number.")

    class Meta:
        order_with_respect_to = 'gender'

    def __str__(self):
        return f"{self.username} {self.last_name}"
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, users):
        return True


    def get_absolute_url(self):
        return reverse(
            "account.user-detail:detail", kwargs={"username": self.username}
        )


class Identity(models.Model):
    user = models.ForeignKey(User, null=True, default="", blank=True, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=550)
    country     = CountryField(blank_label='(select country)', default="")
    id_num      = models.CharField(verbose_name="ID Number", max_length=250)
    issued      = models.DateField(verbose_name="Issued Date", null=True, auto_now_add=False)
    expiration  = models.DateField(verbose_name="Expiry Date", null=True, auto_now_add=False)


    def __str__(self):
        return self.nationality

    class Meta:
        managed = True
        verbose_name = 'National ID'
        verbose_name_plural = 'National IDs'

