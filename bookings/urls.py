from django.urls import path
from . import views


urlpatterns = [
    path('bookings/', views.booking_table, name='bookings'),
    path('booked/', views.booked_view, name='booked'),
    path('mybookings/', views.my_bookings, name='mybookings'),
]