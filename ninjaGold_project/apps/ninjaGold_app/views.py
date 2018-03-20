# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random
import datetime

# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    return render(request,'ninjaGold_app/index.html')

def process_money(request):
    request.session['money'] = request.POST['money']
    def activity(request,gold,action,place):
        timestamp = datetime.datetime.now()
        if place == 'casino':
            if action == 'collect':
                collect = "Entered a casino and won %d golds, you have great LUCK! %s" % (gold, timestamp)
                request.session['activity'].insert(0, ['collect', collect])
            elif action == 'lose':
                lost = "Entered a casino and lost %d golds...... what terrible LUCK... %s" % (gold, timestamp)
                request.session['activity'].insert(0, ['lose', lost])
        elif place == 'farm':
            request.session['activity'].insert(0, ['collect', "Earned %d golds from the farm! %s" % (gold, timestamp)])
        elif place == 'cave':
            request.session['activity'].insert(0, ['collect', "Earned %d golds from the cave! %s" % (gold, timestamp)])
        elif place == 'house':
            request.session['activity'].insert(0, ['collect', "Earned %d golds from the house! %s" % (gold, timestamp)])

    if request.session['money'] == 'farm':
        rand1 = random.randint(10,20)
        request.session['gold'] += rand1
        activity(request, rand1, 'collect', 'farm')
    elif request.session['money'] == 'cave':
        rand1 = random.randint(5,10)
        request.session['gold'] += rand1
        activity(request, rand1, 'collect', 'cave')
    elif request.session['money'] == 'house':
        rand1 = random.randint(2,5)
        request.session['gold'] += rand1
        activity(request, rand1, 'collect', 'house')
    elif request.session['money'] == 'casino':
        rand1 = random.randint(0,20)
        rand2 = random.randint(0,1)
        if rand2 == 0:
            request.session['gold'] += rand1
            activity(request, rand1, 'collect', 'casino')
        elif rand2 == 1:
            request.session['gold'] -= rand1
            activity(request, rand1, 'lose', 'casino')
    return redirect('/main')

def main(request):
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activity'] = []
    return redirect('/')