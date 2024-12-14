from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name=self.scope["url_route"]["kwargs"]['room_name']
        self.room_group_name=f"chat_{self.room_name}"
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        ))
    def receive(self, text_data):
        text=json.loads(text_data)
        msg=text["msg"]
        
        async_to_sync(self.channel_layer.group_send)(self.room_group_name,{
            
            "type": "chat.msg",
            "msg":msg
            

        })
    def chat_msg(self,event):
        msg=event["msg"]
        
        self.send(text_data=json.dumps({
            "msg":msg,
            
        }))
   

       