from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request, 'menu/menu.html')

def menu_drinks(request):
    return render(request, 'menu/drinks.html')
