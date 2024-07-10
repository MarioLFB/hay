from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('drinks/', views.menu_drinks, name='drinks'),
]