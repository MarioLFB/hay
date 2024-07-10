from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('food/', views.menu_food, name='food'),
    path('drinks/', views.menu_drinks, name='drinks'),
]