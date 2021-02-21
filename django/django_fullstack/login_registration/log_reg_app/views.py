from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.validator(request.POST)
    if errors: 
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email_address=request.POST['email_address'],
            password=pw_hash
        )
        request.session['user_id'] = new_user.id
        return redirect('/success')

def login(request):
    user_req = User.objects.filter(email_address=request.POST['email_address'])
    if user_req:
        logged_user = user_req[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id 
            return redirect('/success')
    else:
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')

def success(request):
    if request.method == "GET":
        return redirect('/')
    session_id = request.session['user_id']
    if session_id:
        user = User.objects.filter(id=request.session['user_id'])
        context = {
            'user': user
        }
        return render(request, "success.html", context)
    else: 
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
