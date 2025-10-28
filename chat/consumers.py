import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(
            text_data=json.dumps(
                {
                    "message": "connected sucessfully",
                    "connnetion": "connection established sucessfully",
                }
            )
        )

    def disconnect(self, code):
        pass

   