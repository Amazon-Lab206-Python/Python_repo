# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        'email' : 'noah.hendry1@gmail.com',
        'name' : 'Noah'
    }
    return render(request, 'first_app/index.html', context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == 'POST':
        print 'h'*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
    return redirect('/')

def number(request, number):
    response = 'hello ' + number
    return HttpResponse(response)

# Create your views here.
