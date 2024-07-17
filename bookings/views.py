from django.shortcuts import render, redirect
from .forms import TableForm
from .models import Table
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def login_needed(request):
    '''
    Function to display a message to the user that they need to login to access the page
    '''
    return render(request, 'loginneeded.html')


def booking_table(request):
    '''
    Function to book a table
    '''
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
            messages.success(request, 'Booking made successfully')
            return redirect('booked')
    else:
        form = TableForm()
    return render(request, 'bookings/bookings.html', {'form': form})


def booked_view(request):
    '''
    Function to display a message to the user that their booking was successful
    '''
    if not request.user.is_authenticated:
        return login_needed(request)
    return render(request, 'bookings/booked.html')

@login_required
def my_bookings(request):
    '''
    Function to display all the bookings made by the user
    '''
    bookings = Table.objects.filter(user=request.user)
    return render(request, 'bookings/mybookings.html', {'bookings': bookings})


def delete_bookings(request):
    '''
    Function to delete all the bookings made by the user
    '''
    if request.method == 'POST':
        Table.objects.filter(user=request.user).delete()
        messages.warning(request, 'Booking deleted successfully')
        return redirect('mybookings')
    return render(request, 'bookings/deletebookings.html')

 
def edit_bookings(request, booking_id):
    '''
    Function to edit a booking made by the user
    '''
    booking = Table.objects.get(pk=booking_id)
    form = TableForm(instance=booking)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully')
            return redirect('mybookings')
    return render(request, 'bookings/edit_bookings.html', {'form': form})
    