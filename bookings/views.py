from django.shortcuts import render, redirect
from .forms import TableForm
from .models import Table
from django.contrib.auth.decorators import login_required


@login_required
def booking_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save(commit=False)
            table.user = request.user
            table.save()
            return redirect('booked')
    else:
        form = TableForm()
    return render(request, 'bookings/bookings.html', {'form': form})


def booked_view(request):
    return render(request, 'bookings/booked.html')


@login_required
def my_bookings(request):
    bookings = Table.objects.filter(user=request.user)
    return render(request, 'bookings/mybookings.html', {'bookings': bookings})