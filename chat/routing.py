from django.urls import re_path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'wss/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    
]
