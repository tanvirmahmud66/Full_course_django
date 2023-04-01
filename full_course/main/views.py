from django.shortcuts import render, redirect
from .models import RoomDatabase
from .forms import RoomForm
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def room(request):
    return render(request, 'home/room.html', {"rooms": RoomDatabase.objects.all()})


def room_dynamic(request, pk):
    pk = int(pk)
    details = RoomDatabase.objects.get(id=pk)
    return render(request, 'home/room.html', {"name": details.name, "description": details.description})


def create_room(request):
    forms = RoomForm()
    if request.method == "POST":
        forms = RoomForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('room')
    return render(request, 'home/room_form.html', {"forms": forms})
