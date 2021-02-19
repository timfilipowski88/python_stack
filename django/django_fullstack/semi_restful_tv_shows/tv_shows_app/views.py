from django.shortcuts import render, redirect
from .models import Show
# Create your views here.

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        released = request.POST['released'],
        desc = request.POST['desc'],
    )
    return redirect('/shows')

def show(request, show_id):
    get_show = Show.objects.get(id=show_id)
    context = {
        'show': get_show
    }
    return render(request, "show.html", context)

def edit(request, show_id):
    get_show = Show.objects.get(id=show_id)
    context = {
        'show': get_show
    }
    return render(request, "edit.html", context)

def update(request, show_id):
    get_show = Show.objects.get(id=show_id)
    get_show.title = request.POST['title']
    get_show.network = request.POST['network']
    get_show.released = request.POST['released']
    get_show.desc = request.POST['desc']
    get_show.save()
    return redirect('/shows')

def delete(request, show_id):
    get_show = Show.objects.get(id=show_id)
    get_show.delete()
    return redirect('/shows')

