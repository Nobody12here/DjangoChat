from django.db import models
from account.models import User


class Room(models.Model):
    """Model definition for Room."""

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    admin = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="admin_rooms",
    )  # room owner
    is_private = models.BooleanField(default=False)
    members = models.ManyToManyField(User, blank=True, related_name="chat_rooms")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Room."""

        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.name

    def transfer_admin(self):
        if (
            self.admin not in self.members.all()
        ):  # if the current admin is not in the members list (admin has left the room)
            new_admin = self.members.first()
            if new_admin:
                self.admin = new_admin
                self.save()


class Message(models.Model):
    """Model definition for Message."""

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    text = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Message."""

        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        """Unicode representation of Message."""
        self.sender.last_name
