from django.db import models
from client.models import User


# Create your models here.
class RoomModel(models.Model):
    room_name = models.CharField(max_length=150,unique=True)
    first_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='first')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='second')
    last_message = models.TextField(null=True,blank=True)
    seen = models.IntegerField(null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.room_name+str(self.id)


class MessageModel(models.Model):
    author = models.ForeignKey(User, related_name='m', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    chang = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    seen = models.IntegerField(null=True)

