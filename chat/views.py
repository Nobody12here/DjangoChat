from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message, Room


@login_required
def create_room(request: HttpRequest):
    return render("chat/create_room.html")
    pass
