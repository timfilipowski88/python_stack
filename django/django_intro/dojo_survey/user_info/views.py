from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "name": 'tim',
    }
    print("Request works")
    return render(request, 'index.html', context)

def results(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'lang': request.POST['language'],
            'loc': request.POST['location'],
            'comm': request.POST['comment']
        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')
