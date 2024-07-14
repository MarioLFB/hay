from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from bookings.models import Table

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            
            if password == password_confirm:
                
                if User.objects.filter(username=username).exists():
                    form.add_error('username', 'User already exists')
                else:
                    # Create a new user
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'You have successfully registered. Please login.')
                    return redirect('login')
            else:
                form.add_error('password_confirm', 'Passwords do not match')
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form})

        
def login_view(request):
    error_message = None
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')
            else:
                error_message = 'Invalid username or password.'
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})
    
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('home')
    return render(request, 'logout.html')



@login_required
def profile(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            
            if password == password_confirm:
                user = request.user
                user.username = username
                user.email = email
                user.set_password(password)
                user.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('profile')
            else:
                form.add_error('password_confirm', 'Passwords do not match')
    else:
        initial_data = {
            'username': request.user.username,
            'email': request.user.email
        }
        form = UserRegisterForm(initial=initial_data)
    
    context = {
        'user': request.user,
        'form': form
    }
    
    return render(request, 'profile.html', context)