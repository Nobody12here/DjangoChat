from . import views
from django.urls import path

urlpatterns = [path("create-room/", views.create_room, name="create-room")]
