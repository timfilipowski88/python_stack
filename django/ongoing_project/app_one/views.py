from django.shortcuts import render

# Create your views here.

def index(request): 
    context = {
        "name": "Timbo",
        "fav_activity": "Rock Climbing",
        "fav_foods": ["Granola", "Pasta", "Pizza"]
    }
    return render(request, "index.html", context)