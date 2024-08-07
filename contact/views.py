from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def contact(request):
    '''
    Function to display the contact form
    '''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_sent')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

def message_sent(request):
    '''
    Function to display a message to the user that their message 
    was sent successfully
    '''
    return render(request, 'contact/message_sent.html')
