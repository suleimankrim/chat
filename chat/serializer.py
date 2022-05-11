from rest_framework import serializers
from .models import MessageModel, RoomModel
from client.models import User
from django.db.models import Q
from newauth.serializer import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'


class RoomGetSerializer(serializers.ModelSerializer):
    first_user = serializers.SerializerMethodField()
    second_user = serializers.SerializerMethodField()
    last_message = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = RoomModel
        fields = ['room_name', 'second_user', 'first_user', 'last_message', 'date']

    def get_first_user(self, obj):
        request = self.context['request']
        if request.user.id == obj.first_user.id:
            return obj.first_user.id
        else:
            user = User.objects.get(pk=obj.first_user.id)
            if user.img == '':
                image = None
            else:
                image = user.img
            return {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'img': f'{image}'}

    def get_second_user(self, obj):
        request = self.context['request']
        if request.user.id == obj.second_user.id:
            return obj.second_user.id
        else:
            user = User.objects.get(pk=obj.second_user.id)
            if user.img == '':
                image = None
            else:
                image = user.img
            return {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'img':  f'{image}'
            }


class RoomPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ['room_name', 'second_user']

    def validate_second_user(self, value):
        print("hi")
        request = self.context['request']
        print(request.user.id)
        print(value.id)
        qs = User.objects.filter(id__exact=value.id)
        print('nfd')
        if qs.exists():
            ex = RoomModel.objects.filter(Q(Q(first_user=request.user.id) & Q(second_user=value.id)) | Q(Q(first_user=value.id) & Q(second_user=request.user.id))).exists()
            print(ex)
            if ex:
                raise serializers.ValidationError("Room exist")
            else:
                return value
        else:
            raise serializers.ValidationError("Not Found")
