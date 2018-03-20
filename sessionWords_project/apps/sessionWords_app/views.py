# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime, localtime
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    if 'word_obj' not in request.session:
        request.session['word_obj'] = {}
    if 'words' not in request.session:
        request.session['words'] = []
    if 'style' not in request.session:
        request.session['style'] = ""
    
    return render(request,'sessionWords_app/index.html')

def process(request):
    if 'bold' not in request.POST:
        request.session["bold"] = 'normal'
    else:
        request.session["bold"] = 'bold'
    if 'color' not in request.POST:
        request.session["color"] = 'black'
    else:
        request.session["color"] = request.POST['color']
    #request.session['word'].append("<p class='word' style='color:"+str(request.POST['color'])+"; font-weight:"+str(request.session['bold'])+"'>"+str(request.POST['word'])+"</p><p class='time'>- added on "+str(strftime("%Y-%m-%d %H:%M %p", gmtime()))+"</p>")

    request.session['style'] = 'style=color:'+str(request.session['color'])+';font-weight:'+str(request.session['bold'])

    request.session['word_obj'] = {
        'word' : str(request.POST['word']),
        'style' : request.session['style'],
        'time' : str(strftime("%Y-%m-%d %H:%M %p", localtime()))
    }
    
    request.session['words'].append(request.session['word_obj'])
    request.session.modified = True

    return redirect('/show')

def show(request):
    context = {
        "string" : request.session['words'],
    }
    return render(request,'sessionWords_app/index.html', context)
    
def clear(request):
    request.session.clear()
    return redirect('/')