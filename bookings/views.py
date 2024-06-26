from django.shortcuts import render, redirect
from .forms import TableForm
from .models import Table

def booking_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booked')
    else:
        form = TableForm()
    return render(request, 'bookings/bookings.html', {'form': form})


def booked_view(request):
    return render(request, 'bookings/booked.html')

def my_bookings(request):
    bookings = Table.objects.all()
    return render(request, 'bookings/mybookings.html', {'bookings': bookings})