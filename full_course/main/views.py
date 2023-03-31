from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {"id": 1, "name": "Tanvir"},
    {"id": 2, "name": "Mahmud"},
    {"id": 3, "name": "Fahim"},
]


def home(request):
    return render(request, 'home/home.html')


def room(request):
    return render(request, 'home/room.html', {"rooms": rooms})


def room_dynamic(request, pk):
    return render(request, 'home/room.html', {"name": pk})
