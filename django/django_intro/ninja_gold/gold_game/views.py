from django.shortcuts import render, redirect
import random
from datetime import datetime


# Create your views here.


def index(request):
    if 'total' not in request.session or 'activity' not in request.session: 
        request.session['total'] = 0
        request.session['activity'] = []
    return render(request, 'index.html')

def reset(request):
    request.session['total'] = 0
    request.session['activity'] = []
    return redirect("/")

def process(request):
    if request.method == 'POST':
        if request.POST['location'] == 'farm':
            gold = random.randint(10, 20)
            request.session['total'] += gold
            request.session['activity'].append('You earned ' + str(gold) + ' golds from the ' + request.POST['location'] + (' ') + str(datetime.now().strftime("%Y-%m-%d %H:%M")))
            return redirect("/")
        elif request.POST['location'] == 'cave':
            gold = random.randint(5, 10)
            request.session['total'] += gold
            request.session['activity'].append('You earned ' + str(gold) + ' golds from the ' + request.POST['location'] + (' ') + str(datetime.now().strftime("%Y-%m-%d %H:%M")))
            return redirect("/")
        elif request.POST['location'] == 'house':
            gold = random.randint(2, 5)
            request.session['total'] += gold
            request.session['activity'].append('You earned ' + str(gold) + ' golds from the ' + request.POST['location'] + (' ') + str(datetime.now().strftime("%Y-%m-%d %H:%M")))
            return redirect("/")
        elif request.POST['location'] == 'casino':
            if request.session['total'] >= 0:
                gold = random.randint(-50, 50)
                request.session['total'] += gold
                if gold >= 0: 
                    request.session['activity'].append('You earned ' + str(gold) + ' golds from the ' + request.POST['location'] + (' ') + str(datetime.now().strftime("%Y-%m-%d %H:%M")))
                else: 
                    request.session['activity'].append('You lost ' + str(gold) + ' golds to the ' + request.POST['location'] + (' ') + str(datetime.now().strftime("%Y-%m-%d %H:%M")))
            return redirect("/")
        else:
            print('not farm')
            return redirect("/")