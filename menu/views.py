from django.shortcuts import render

# Create your views here.

def menu(request):
    '''
    Function to display the menu page
    '''
    return render(request, 'menu/menu.html')

def menu_drinks(request):
    '''
    Function to display the drinks page
    '''
    return render(request, 'menu/drinks.html')
