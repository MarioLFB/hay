from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm

# Create your views here.
 
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'User already exists'})
        else:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')

        
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