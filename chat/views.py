from django.db.models import Q
from .models import RoomModel
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RoomPostSerializer,RoomGetSerializer
from rest_framework import generics


class Index(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        s = 'suliman'
        print(request.user.id)
        return Response({'p': request.user.id}, template_name='index.html')


class Room(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, room_name):
        print(request.user.id)
        return Response({'room_name': room_name, 'p': request.user.id}, template_name='room.html')


class RoomGetView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RoomGetSerializer

    def get_queryset(self):
        pk = self.request.user.id
        print(pk)
        return RoomModel.objects.filter(Q(first_user=pk) | Q(second_user=pk))


class RoomPostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RoomPostSerializer

    def perform_create(self, serializer):
        print(self.request.user.id)
        return serializer.save(first_user=self.request.user)
