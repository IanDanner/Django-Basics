# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    return render(request,'surveyForm_app/index.html')

def process(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else: 
        request.session['count'] = 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/results')

def results(request):
    return render(request,'surveyForm_app/results.html')

def back(request):
    return redirect('/')