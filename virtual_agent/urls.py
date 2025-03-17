from django.urls import path
from .views import chat_with_ai, chat_interface

urlpatterns = [
    path('chat_with_ai/', chat_with_ai, name='chat_with_ai'),
    path('chat_interface/', chat_interface, name='chat_interface'),
]
