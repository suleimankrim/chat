from django.urls import path

from knox.views import LogoutView

from .views import UserAPIView, RegisterAPIView, LoginAPIView,UserFind
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('user', UserAPIView.as_view()),
    path('friend', UserFind.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout'),
    path('docs', include_docs_urls(title="Whats Upp")),
    path('', get_schema_view(
        title="Whats Upp",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),


]
