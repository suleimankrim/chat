from django.urls import path
from .views import CodeView
urlpatterns = [
    path('',CodeView.as_view())
]