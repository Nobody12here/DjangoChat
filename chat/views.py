from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message, Room
from .forms import ChatRoomForm


@login_required(login_url="/account")
def create_room(request: HttpRequest):
    room_form = ChatRoomForm()
    if request.method == "POST":
        room_form = ChatRoomForm(request.POST)
        if room_form.is_valid():
            room_form.save()
            return render(request, "chat/create_room.html")
    context = {"room_form": room_form}
    return render(request, "chat/create_room.html", context)
