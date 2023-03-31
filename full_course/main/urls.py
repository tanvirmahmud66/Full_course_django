from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
    path('room/<str:pk>/', views.room_dynamic, name='room_dynamic_route'),
]
