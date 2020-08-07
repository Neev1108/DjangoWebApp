from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .import forms
# Create your views here.

def account_list(request):
    accounts = Account.objects.all().order_by("date_created")
    return render(request, 'accounts/see_accounts.html', {"accounts": accounts})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('http://127.0.0.1:8000/accounts/bank-account-menu')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            return redirect('http://127.0.0.1:8000/accounts/bank-account-menu')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('http://127.0.0.1:8000')
    
    
@login_required(login_url= "http://127.0.0.1:8000/accounts/login/")
def BA_menu(request):
    accounts = Account.objects.filter(customer = request.user).order_by("date_created")
    return render(request, 'accounts/BA_menu.html', {"accounts": accounts})

@login_required(login_url= "http://127.0.0.1:8000/accounts/login/")
def createAccount(request):
    if request.method == 'POST':
        form = forms.CreateAccount(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = request.user
            instance.save()
            return redirect('http://127.0.0.1:8000/accounts/bank-account-menu/')
    else:
        form = forms.CreateAccount()
    return render(request, 'accounts/createAccount.html', {'form': form})