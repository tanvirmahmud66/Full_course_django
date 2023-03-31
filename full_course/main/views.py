from django.shortcuts import render
from .models import RoomDatabase
# Create your views here.

rooms = [
    {"id": 1, "name": "Tanvir"},
    {"id": 2, "name": "Mahmud"},
    {"id": 3, "name": "Fahim"},
]


def home(request):
    return render(request, 'home/home.html')


def room(request):
    return render(request, 'home/room.html', {"rooms": RoomDatabase.objects.all()})


def room_dynamic(request, pk):
    pk = int(pk)
    details = RoomDatabase.objects.get(id=pk)
    return render(request, 'home/room.html', {"name": details.name, "description": details.description})
