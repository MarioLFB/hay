from django.shortcuts import render

# Create your views here.

def home(request):
    '''
    Function to display the home page
    '''
    return render(request, 'home/home.html')
