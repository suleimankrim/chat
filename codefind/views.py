from rest_framework import generics
from .serializer import CodeSerializer
from .models import CodeModel
from client.models import User
from rest_framework import permissions


class CodeView(generics.CreateAPIView):
    serializer_class = CodeSerializer
    queryset = CodeModel
    permission_classes = [permissions.AllowAny]

    def perform_create(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        code = CodeModel.objects.get(instance=user)
        if code.number == request.number:
            print("ok")
        else:
            print("no")
