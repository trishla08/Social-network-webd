from django.conf.urls import url
 
from chat import views

app_name = 'chatapp'
 
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^chat/(?P<id>\d+)/$', views.chat_room, name='chat_room'),
]