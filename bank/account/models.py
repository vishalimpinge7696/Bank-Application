from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import (MinValueValidator, MaxValueValidator, RegexValidator)
from datetime import datetime

# Create your models here.

choices = [
    ("Male", "Male"),
    ('Female', 'Female')

]
achoice = [

          ("Single Account", "Single Account"),
          ("Joint Account", "Joint Account")
      ]


class UserProfile(AbstractUser):
    username = models.CharField('username', unique=True, max_length=30,  default="")
    full_name = models.CharField(max_length=50, default="",blank= False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    father_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=False)
    mother_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=choices)
    account_type = models.CharField(max_length=20, choices=achoice)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    address = models.TextField(max_length=110)
    account_number = models.ForeignKey('Account_Number', on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.BigIntegerField(null=True, blank=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']
    class Meta:
        db_table = "users"
        verbose_name_plural = 'USER_PROFILE'
        managed = True

    def __str__(self):
        return str(self.username)


class Account_Number (models.Model):
    account_number = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=150, default=None)

    class Meta:
        db_table = "acc_no"
        verbose_name_plural = 'ACCOUNT_NUMBER'
        managed = True

    def __str__(self):
        return str(self.account_number)


class Transactions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transaction"
        verbose_name_plural = 'TRANSACTION'
        managed = True

    def __str__(self):
        return str(self.amount)


class Transfer_Money(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    Recipient_Name = models.CharField(max_length=110)
    amount = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    account_no = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(10000), MaxValueValidator(99999999999999999)])
    IFSC= models.CharField(max_length=110)
    date = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table = 'transfer_money'
        verbose_name_plural = 'TRANSFEr_MONEY'
        managed = True

    def __str__(self):
        return str(self.id)