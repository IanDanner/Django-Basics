# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    if 'price' not in request.session:
        request.session['price'] = 0
    if 'item_price' not in request.session:
        request.session['item_price'] = 0
    if 'total_amount' not in request.session:
        request.session['total_amount'] = 0
    if 'total_price' not in request.session:
        request.session['total_price'] = 0
    return render(request,'amadon_app/index.html')

def process(request):
    item_id = [101,102,103,104]
    item_price = [19.99,29.99,4.99,49.99]
    for idx in range(0,len(item_id)):
        if item_id[idx] == int(request.POST['id']):
            request.session['price'] = item_price[idx]

    request.session['item_price'] = request.session['price'] * int(request.POST['amount'])
    request.session['total_price'] = request.session['total_price'] + request.session['item_price']
    request.session['total_amount'] = request.session['total_amount'] + int(request.POST['amount'])
    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')
    