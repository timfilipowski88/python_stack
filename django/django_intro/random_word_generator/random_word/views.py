from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    request.session['random_word'] = get_random_string(length=14)
    return render(request, 'index.html')



def reset(request):
    request.session.flush()
    return redirect('/random_word')