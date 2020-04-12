from django.contrib import admin
from .models import UserProfile, Account_Number, Transactions
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Account_Number)
admin.site.register(Transactions)