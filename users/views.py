from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
 
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return HttpResponse('User already exists')
        else:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('home')
        

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponse('You are now logged in.')
        else:
            return HttpResponse('Invalid login credentials.')
    else:
        return render(request, 'login.html')