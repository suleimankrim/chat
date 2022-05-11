# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('web/<str:room_name>/', views.Room.as_view()),
    path('room/get/', views.RoomGetView.as_view()),
    path('room/post/', views.RoomPostView.as_view()),
]