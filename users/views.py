from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm

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
                return redirect('home')  # Redirecionar para a página de sucesso após o login
            else:
                error_message = 'Invalid username or password.'
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})
    
@login_required
def profile(request):
    return render(request, 'profile.html')