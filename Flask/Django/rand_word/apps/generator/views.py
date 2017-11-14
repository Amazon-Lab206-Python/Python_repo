# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

def index(request):
    try:
        request.session['counter']
    except:
        request.session['counter'] = 0
    
    context= {
        'rand': get_random_string(length=14)
    }
    return render(request, 'generator/index.html', context)

def random(request):
    request.session['counter'] += 1
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    return redirect('/')