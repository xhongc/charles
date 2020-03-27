import json
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer

from charles.chat.models import ChatLog, ChatRoom
from utils.tulingrobot import sizhi


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super(ChatConsumer, self).__init__(*args, **kwargs)
        self.room_name = 'chat'
        self.room_group_name = 'chat'

    async def connect(self):
        room_channel_no = self.scope['url_route']['kwargs']['room_name']
        if self.scope["user"].is_anonymous:
            # Reject the connection
            await self.close()
        elif room_channel_no in self.scope["user"].profile.get_my_chat_room():
            # Reject the connection
            self.room_name = room_channel_no
            self.room_group_name = 'chat_%s' % self.room_name

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        msg_type = text_data_json['msg_type']
        chat_user = self.scope.get('user')
        send_time = datetime.now()
        if msg_type == 'chat_message':
            if self.room_name.isdigit():
                pass
            else:
                char_room = ChatRoom.objects.filter(channel_no=self.room_name).first()
                if message:
                    ChatLog.objects.create(chat_datetime=send_time,
                                           content=message,
                                           msg_type=msg_type,
                                           who_said=chat_user,
                                           said_to_room=char_room)
        elif msg_type == 'chat_info':
            pass
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': str(chat_user.id),
                'send_time': send_time.strftime('%p %H:%M'),
                'msg_type': msg_type,
                'username': self.scope.get('user').username
            }
        )
        if self.room_name == 'robot' and msg_type == 'chat_message':
            robot_msg = sizhi(message)
            robot_user = User.objects.filter(username='robot').first()
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': robot_msg,
                    'user_id': 'robot',
                    'send_time': send_time.strftime('%p %H:%M'),
                    'msg_type': msg_type,
                    'username': self.scope.get('user').username
                }
            )
            if self.room_name.isdigit():
                pass
            else:
                char_room = ChatRoom.objects.filter(channel_no=self.room_name).first()
                if message:
                    ChatLog.objects.create(chat_datetime=send_time,
                                           content=robot_msg,
                                           msg_type=msg_type,
                                           who_said=robot_user,
                                           said_to_room=char_room)

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']
        send_time = event['send_time']
        type = event['type']
        msg_type = event['msg_type']
        username = event['username']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user_id': user_id,
            'send_time': send_time,
            'type': type,
            'msg_type': msg_type,
            'username': username,
        }))
