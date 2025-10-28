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
            chat_room.members.add(request.user)
            return redirect("list-rooms")
    else:
        room_form = ChatRoomForm()

    context = {"room_form": room_form}
    return render(request, "chat/create_room.html", context)


@login_required(login_url="/account")
def join_room(request: HttpRequest, room_id: str = None):
    if room_id:
        try:
            room = Room.objects.get(id=room_id)
            if request.user not in room.members.all():
                room.members.add(request.user)
            context = {
                "room_name": room.name,
            }
            return redirect("list-rooms")  # redirect to chat interface

        except Room.DoesNotExist:
            return redirect("list-rooms")
    else:
        try:
            rooms = Room.objects.filter(is_private=False)
            context = {"rooms": rooms}
            return render(request, "chat/join_room.html", context)
        except Room.DoesNotExist:
            return redirect("list-rooms")


@login_required(login_url="/account")
def list_rooms(request: HttpRequest):
    rooms = Room.objects.filter(admin=request.user)
    context = {"rooms": rooms}
    return render(request, "chat/list_rooms.html", context)


@login_required(login_url="/account")
def room(request: HttpRequest, room_id: int):
    try:
        room = Room.objects.get(id=room_id)
        
    except Room.DoesNotExist:
        print(f"this room id does not exists {room_id}")

    return render(request, "chat/room.html")
