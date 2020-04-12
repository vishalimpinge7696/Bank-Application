from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_view', views.register_view, name='register_view'),
    path('user_login', views.user_login, name='user_login'),
    path('account_details', views.account_details, name='account_details'),
    path('account_balance', views.account_balance, name='account_balance'),
    path('transfer', views.transfer, name='transfer'),
    path('transfer_money', views.transfer_money, name='transfer_money'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('logout', views.logout, name='logout'),
    path('deposit', views.deposit, name="deposit"),
    path('withdraw', views.withdraw, name='withdraw'),

]