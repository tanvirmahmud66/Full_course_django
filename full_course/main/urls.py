from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('room/', views.room, name='room'),
    path('room/<str:pk>/', views.room_dynamic, name='room_dynamic_route'),
    path('create-room/', views.create_room, name='create-room'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-room/<str:pk>/', views.delete_room, name="delete-room"),
]
