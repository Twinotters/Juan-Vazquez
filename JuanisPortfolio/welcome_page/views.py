from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



def index(request):
    return render(request, 'welcome_page.html')




