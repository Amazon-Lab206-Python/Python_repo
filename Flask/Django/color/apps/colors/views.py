# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    try:
        request.session['words']
    except:
        request.session['words'] = []
    return redirect('/session_words')

def words(request):
    return render(request,'colors/words.html')

def add_word(request):
    if request.method == 'POST':
        print request.POST
        if 'big' in request.POST:
            big = True
        else:
            big = False

        time = datetime.datetime.now().strftime('%I:%M:%S %p, %B %d, %Y')

        word_builder = {
            'word' : request.POST['word'],
            'color': request.POST['color'],
            'big': big,
            'date': time
        }
        x = request.session['words']
        x.append(word_builder)
        request.session['words'] = x
        print request.session['words']
    return redirect('/session_words')

# Create your views here.
