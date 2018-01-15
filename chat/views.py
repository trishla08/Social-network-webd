from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
 
from chat.models import ChatRoom
 
def index(request):
  chat_rooms = ChatRoom.objects.order_by('name')[:5]
  context = {
    'chat_list': chat_rooms,
  }
  return render(request,'chatapp/index.html', context)
 
def chat_room(request, id):
  chat = get_object_or_404(ChatRoom, pk=id)
  return render(request, 'chatapp/chatroom.html', {'chat': chat})
