
from django.http import HttpResponse
from django.shortcuts import render

def go_homePage(request):
    return render(request, 'accounts/login.html')