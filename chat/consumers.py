import json
from typing import List
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = 17
        print(self.room_id)
        self.accept()
        self.send(
            text_data=json.dumps(
                {
                    "message": "connected sucessfully",
                    "connnetion": "connection established sucessfully",
                }
            )
        )
        messages = await self.get_room_messages()
        self.send(
            text_data=json.dumps({"type": "messages_history", "messages": messages})
        )

    def disconnect(self, code):
        pass

    @database_sync_to_async
    def get_room_messages(self):
        try:
            message_list = []
            room = Room.objects.get(name="private room")
            messages: List[Message] = room.messages.all()

            for message in messages:
                profile_picture = None
                if (
                    hasattr(message.sender, "profile")
                    and message.sender.profile.profile_picture
                ):
                    profile_picture = message.sender.profile.profile_picture.url
                message_list.append(
                    {
                        "message": message.text,
                        "sent_at": message.created_at.strftime('%I:%M %p'),
                        "sender": message.sender.first_name + message.sender.last_name,
                        "profile_picture": profile_picture,
                    }
                )
            print(message_list)
            return message_list
        except Room.DoesNotExist:
            raise ("Room does not exists")
