from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect

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
            # Cria um novo usuário
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('home')  # Redireciona para a página inicial após o registro bem-sucedido









def login(request):
    return render(request, 'login.html')