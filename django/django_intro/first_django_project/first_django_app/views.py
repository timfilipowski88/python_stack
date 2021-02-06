from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Placeholder to later display a list of blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"Placeholder to dipslay blog number: {number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog number {number}")

def destroy(request, number):
    return redirect('/')