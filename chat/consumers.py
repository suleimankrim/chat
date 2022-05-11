# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import MessageModel, User, RoomModel
from django.db.models import Q


class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        print("fitch")
        print(self.room_name)
        messages = MessageModel.objects.order_by('-date').filter(room=self.room_name)[:10]
        content = {
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        print("new")
        author = data['word']
        print(author)
        message = MessageModel.objects.create(
            author_id=author,
            content=data['message'],
            room_id=self.room_name
        )
        print('done')
        content = {
            'messages': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': str(message.author),
            'content': message.content,
            'date': str(message.date),
            'room': self.room_name
        }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print("groub")
        print(self.room_group_name)
        print(self.channel_name)
        print("channal")

        self.accept()
        self.fetch_messages('j')

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        the_room = RoomModel.objects.get(pk=self.room_name)
        messages = MessageModel.objects.filter(room=self.room_name).latest('date')
        print('diction')
        print(the_room)
        print('message')
        print(messages)
        the_room.last_message = messages.content
        the_room.date = messages.date
        the_room.save()

    # Receive message from WebSocket
    def receive(self, text_data):
        print("retrive")
        data = json.loads(text_data)
        self.new_message(data)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def send_message(self, message):
        x = message['messages']
        for i in x:
            self.send(text_data=json.dumps(i))

    def chat_message(self, event):
        print("chat_message")
        message = event['message']
        print(message)
        messagee = message['messages']
        self.send(text_data=json.dumps(messagee))
