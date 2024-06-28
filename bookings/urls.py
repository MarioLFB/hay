from django.urls import path
from . import views


urlpatterns = [
    path('bookings/', views.booking_table, name='bookings'),
    path('booked/', views.booked_view, name='booked'),
    path('mybookings/', views.my_bookings, name='mybookings'),
    path('delete_bookings/<booking_id>', views.delete_bookings, name='delete-bookings'),
    path('edit_bookings/<booking_id>', views.edit_bookings, name='edit-bookings'),
    path('loginneeded/', views.login_needed, name='login_needed'),
]