from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('menu/', include('menu.urls')),
    path('bookings/', include('bookings.urls')),
    path('contact/', include('contact.urls')),
    path('accounts/', include('users.urls')),
    ]


handler404 = 'home.views.handler404'