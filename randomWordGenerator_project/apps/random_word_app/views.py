# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    return render(request,'random_word_app/index.html')

def gen_random(request):
    if 'num' in request.session:
        request.session['num'] += 1
    else: 
        request.session['num'] = 1
    context = {
        "word" : get_random_string(length=14),
    }
    return render(request,'random_word_app/index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')