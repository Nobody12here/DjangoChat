from . import views
from django.urls import path

urlpatterns = [
    path("create-room/", views.create_room, name="create-room"),
    path(
        "",
        views.list_rooms,
        name="list-rooms",
    ),
    path(
        "join-rooms/",
        views.join_room,
        name="join-room",
    ),
    path(
        "join-rooms/<str:room_id>",
        views.join_room,
        name="join-room",
    ),
    path("room/<int:room_id>", views.room, name="room"),
]
