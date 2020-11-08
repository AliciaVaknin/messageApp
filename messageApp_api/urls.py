from django.urls import path

from . import views



app_name = 'messageApp_api'
urlpatterns = [
    path('get_all_messages/', views.get_all_messages, name='get_all_messages'),
    path('create_message/', views.create_message, name='create_message'),
    #path('<int:msg_id>/<str:email>/get_message/', views.get_message, name='get_message'),
    #path('<int:msg_id>/<str:email>/delete_message/', views.delete_message, name='delete_message'),
    #path('<str:sender>/<str:reciever>/<str:subject>/<str:message>/create_message/', views.create_message, name='create_message'),
    #path('messages/', views.MessageList.as_view()),
    #path('messages/get_all_messages', views.MessageList.get_all_messages),
]