from django.shortcuts import render, redirect
from .models import RoomDatabase, Topic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .forms import RoomForm
# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('room')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('room')
        else:
            messages.error(request, 'username or password does not exist')
    return render(request, 'home/login_reg.html')


def logout_page(request):
    logout(request)
    return redirect('room')


@login_required(login_url='login')
def room(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = RoomDatabase.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    dic = {
        "rooms": rooms,
        "topics": topics,
        "room_count": room_count,
    }
    return render(request, 'home/room.html', context=dic)


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


@login_required(login_url='login')
def update_room(request, pk):
    room = RoomDatabase.objects.get(id=pk)
    forms = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse("you are not allow here")
    if request.method == "POST":
        forms = RoomForm(request.POST, instance=room)
        if forms.is_valid():
            forms.save()
            return redirect('room')
    return render(request, 'home/room_form.html', {"forms": forms})


@login_required(login_url='login')
def delete_room(request, pk):
    room = RoomDatabase.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("you are not allow here")
    if request.method == "POST":
        room.delete()
        return redirect('room')
    return render(request, 'home/delete.html', {"obj": room})
