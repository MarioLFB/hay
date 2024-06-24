from django.shortcuts import render, redirect
from .forms import TableForm


# Create your views here.

def booking_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    else:
        form = TableForm()
    return render(request, 'bookings/bookings.html', {'form': form})
    
        
    