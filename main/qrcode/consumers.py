from django.urls.conf import path
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = "test_consumer"
        self.group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data = json.dumps({
            'status' : 'connected'
        }))
        # self.close() 

    def receive(self, text_data=None, bytes_data=None):
        print(text_data)

    def disconnect(self, close_code):
        # Called when the socket closes
        pass