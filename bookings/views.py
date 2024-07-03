from django.shortcuts import render, redirect
from .forms import TableForm
from .models import Table
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def login_needed(request):
    return render(request, 'loginneeded.html')


def booking_table(request):
    if not request.user.is_authenticated:
        return login_needed(request)
    
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save(commit=False)
            table.user = request.user
            if Table.objects.filter(user=request.user).exists():
                messages.error(request, "You have already made a booking. You can only make one booking at a time.")
                return redirect('mybookings')
            table.save()
            return redirect('booked')
    else:
        form = TableForm()
    return render(request, 'bookings/bookings.html', {'form': form})


def booked_view(request):
    if not request.user.is_authenticated:
        return login_needed(request)
    return render(request, 'bookings/booked.html')

@login_required
def my_bookings(request):
    bookings = Table.objects.filter(user=request.user)
    return render(request, 'bookings/mybookings.html', {'bookings': bookings})


def delete_bookings(request, booking_id):
    booking = Table.objects.get(pk=booking_id)
    booking.delete()
    return redirect('mybookings')

def edit_bookings(request, booking_id):
    booking = Table.objects.get(pk=booking_id)
    form = TableForm(instance=booking)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully')
            return redirect('mybookings')
    return render(request, 'bookings/edit_bookings.html', {'form': form})
    