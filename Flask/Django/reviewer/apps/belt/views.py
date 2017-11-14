# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'belt/index.html')

def register(request):
    result = User.objects.validate(request.POST)
    if result[0]:
        all_users = User.objects.all()
        context = {
            'all_users': all_users
        }
        return render(request,'belt/homepage.html', context)
    else:
        for error in result[1]:
            messages.add_message(request,messages.INFO, error)
        return redirect('/')

def login(request):
    result = User.objects.login(request.POST)
    if result[0]:
        all_users = User.objects.all()
        context = {
            'all_users': all_users
        }
        return render(request,'belt/homepage.html', context)
    else:
        for error in result[1]:
            messages.add_message(request,messages.INFO, error)
            return redirect('/')
    
        
        

# Create your views here.