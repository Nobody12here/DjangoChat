from django import forms
from .models import Room


class ChatRoomForm(forms.ModelForm):
    """Form definition for ChatRoom."""

    class Meta:
        """Meta definition for ChatRoomform."""

        model = Room
        fields = ("name", "description", "is_private")
    