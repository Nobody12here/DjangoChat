from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room
from .forms import ChatRoomForm


@login_required(login_url="/account")
def create_room(request: HttpRequest):
    if request.method == "POST":
        room_form = ChatRoomForm(request.POST)
        if room_form.is_valid():
            chat_room: Room = room_form.save(commit=False)
            chat_room.admin = request.user
            chat_room.save()
            return redirect("list-rooms")
    else:
        room_form = ChatRoomForm()

    context = {"room_form": room_form}
    return render(request, "chat/create_room.html", context)


@login_required(login_url="/account")
def list_rooms(request: HttpRequest):
    rooms = Room.objects.filter(admin=request.user)
    context = {"rooms": rooms}
    return render(request, "chat/list_rooms.html", context)
