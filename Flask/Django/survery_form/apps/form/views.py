# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
        
    return render(request, 'form/index.html')

def results(request):
    
    return render(request, 'form/results.html')

def process(request):
    try:
        request.session['counter']
    except:
        request.session['counter'] = 0
    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['comment'] = request.POST['comment']
    request.session['counter'] += 1
    return redirect('/results')

# Create your views here.
