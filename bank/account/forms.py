from django import forms
from django.contrib.auth.models import User
from django.core.validators import (MinValueValidator, MaxValueValidator)
from .models import UserProfile, Transactions, Transfer_Money
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Username"}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Email"}))

    full_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Full Name"}))

    phone = forms.IntegerField(max_value=10000000000, required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Contact"}))

    father_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Fathers name"}))

    mother_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Mothers name'}))
    achoice = [

        ("Single Account", "Single Account"),
        ("Joint Account", "Joint Account")
    ]

    account_type = forms.TypedChoiceField(required=True, choices=achoice, widget=forms.Select(
        attrs={'class': 'form-control'}))

    choices = [
        ("Male", "Male"),
        ('Female', 'Female')

    ]
    gender = forms.TypedChoiceField(required=True, choices=choices, widget=forms.
                                    Select(attrs={'class': 'form-control'}))

    YEARS = [x for x in range(1940, 2021)]

    date_of_birth = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))

    address = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Address'}))

    city = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the City'}))

    state = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the State'}))

    pincode = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Pincode'}))

    class Meta:
        model = UserProfile
        fields = {'username', 'full_name', 'father_name', 'mother_name', 'phone', 'email', 'gender', 'date_of_birth',
                  'address', 'city', 'state', 'pincode', 'account_type'}

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):

    phone = forms.IntegerField(max_value=10000000000, required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Contact"}))

    address = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Address'}))

    city = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the City'}))

    state = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the State'}))

    pincode = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Pincode'}))


    class Meta:
        model = UserProfile
        fields = {"phone", 'city', 'state', 'pincode', 'address'}


class DepositForm(forms.ModelForm):
    amount = forms.IntegerField(max_value=100000000, required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Amount to be Deposited"}))

    class Meta:
        model = Transactions
        fields = [
            'amount'
        ]


class WithdrawForm(forms.ModelForm):
    amount = forms.IntegerField(max_value=100000, required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': "Enter the Amount to be Withdrawn"}))

    class Meta:
        model = Transactions
        fields = [
            'amount'
        ]


class TransferMoneyForm(forms.ModelForm):

    Recipient_Name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Recipient Name'}))

    IFSC = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the IFSC Code'}))

    account_no = forms.IntegerField(validators=[
            MinValueValidator(100000),
            MaxValueValidator(99999999999999999)
        ], required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Account No.'}))

    amount = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Amount'}))

    class Meta:
        model = Transfer_Money
        fields = {'Recipient_Name', 'IFSC', 'account_no', 'amount'}