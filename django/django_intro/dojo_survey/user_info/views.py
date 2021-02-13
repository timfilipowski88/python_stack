from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    print("Request works")
    return render(request, 'index.html')

def results(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['lang'] = request.POST['language']
        request.session['loc'] = request.POST['location']
        request.session['comm'] = request.POST['comment']
        return redirect('/results')
    return render(request, 'results.html')
