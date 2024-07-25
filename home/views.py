from django.shortcuts import render

# Create your views here.

def home(request):
    '''
    Function to display the home page
    '''
    return render(request, 'home/home.html')

def handler404(request, exception):
    '''
    Function to handle 404 errors
    '''
    return render(request, '404.html', status=404)
