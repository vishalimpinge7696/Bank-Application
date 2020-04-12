from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Account_Number
import random
# Create your views here.


@login_required(login_url='user_login')
def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        title = "Create a Bank Account"
        form = UserRegistrationForm(
            request.POST or None,
            request.FILES or None
            )

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)

            messages.add_message(request, messages.INFO, 'User Successfully Register.')
            return redirect("account_details")

        context = {"title": title, "form": form}

        return render(request, "signup.html", context)


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.add_message(request, messages.INFO, 'User Successfully Login.')
            return HttpResponseRedirect(reverse('account_details'))
        else:
            messages.add_message(request, messages.INFO, 'The username and/or password you specified are not correct.')
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)


@login_required(login_url='user_login')
def logout(request):
    auth_logout(request)
    return redirect('user_login')


def randomGen():
    return int(random.uniform(10000000, 99999999))


@login_required(login_url='user_login')
def account_details(request):
    try:
        curr_user = Account_Number.objects.get(user_name=request.user)
    except:
        curr_user = Account_Number()
        curr_user.account_number = randomGen()
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "account_details.html", {"curr_user": curr_user})


@login_required(login_url='user_login')
def account_balance(request):
    return render(request, "account_balance.html")


@login_required(login_url='user_login')
def transfer(request):
    return render(request, "transfer.html")


def deposit(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        title = "Deposit"
        form = DepositForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.user.balance += deposit.amount
            deposit.user.save()
            deposit.save()
            messages.success(request, 'You Have Deposited {} Rs.'.format(deposit.amount))
            return redirect("home")

        context = {
                    "title": title,
                    "form": form
                  }
        return render(request, 'with_dep.html', context)


def withdraw(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        title = "Withdrawl"
        form = WithdrawForm(request.POST or None)

        if form.is_valid():
            withdrawal = form.save(commit=False)
            withdrawal.user = request.user

            if withdrawal.user.balance >= withdrawal.amount:

                withdrawal.user.balance -= withdrawal.amount
                withdrawal.user.save()
                withdrawal.save()
                return redirect("home")

            else:
                return render(request, "Error You Can't Withdraw Please Return To Previous Page"
                )

        context = {
                    "title": title,
                    "form": form
                  }
        return render(request, "with_dep.html", context)


def transfer_money(request):
    if request.method == 'POST':
        form = TransferMoneyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Payment Successfully Done !!!')
            return redirect('home')
    else:
        form = TransferMoneyForm()
    return render(request, 'transfer_money.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
    context = {
        'p_form': p_form
    }
    return render(request, 'edit_profile.html', context)