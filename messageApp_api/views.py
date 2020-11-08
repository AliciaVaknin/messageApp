from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
import json

from .models import Message
from .serializers import MessageSerializer


class MessageList(APIView):


    @csrf_exempt
    def get_all_messages(self, request):
        json_data = json.loads(request.body)
        print(json_data)
        msgs_list = Message.objects.filter(reciever=json_data['email'])
        serializer2 = MessageSerializer(msgs_list, many=True)
        return Response(serializer2.data)

    def post(self):
        pass

# @csrf_exempt
# def get_all_messages(request):
#     all_msgs_str = ''
#     json_data = json.loads(request.body)
#     msgs_list = Message.objects.filter(reciever=json_data['email'])
#     for msg in msgs_list:
#         all_msgs_str += f'**** from {msg.sender} ,subject: {msg.subject} body: {msg.message} in date {msg.creation_date} \n'
#     return HttpResponse(all_msgs_str)

@csrf_exempt
def get_all_messages(request):
    json_data = json.loads(request.body)
    msgs_list = Message.objects.filter(reciever=json_data['email'])
    serializer2 = MessageSerializer(msgs_list, many=True)
    return HttpResponse(json.dumps(serializer2.data), content_type='application/json')

"""
def get_all_unread_messages(request, email):
    all_msgs_str = ''
    msgs_list = Message.objects.filter(reciever=email, is_read=False)
    for msg in msgs_list:
        all_msgs_str += f'**** from {msg.sender} ,subject: {msg.subject} body: {msg.message} in date {msg.creation_date} \n'
    #msg = {'from: {msg.sender} ,subject: {msg.subject} body: {msg.message} in date {msg.creation_date} \n'
    return HttpResponse(all_msgs_str)


def get_message(request, email, msg_id):
    all_msgs_str = ''
    msgs_list = Message.objects.filter(reciever=email, id=msg_id)
    for msg in msgs_list:
        all_msgs_str += f'**** from {msg.sender} ,subject: {msg.subject} body: {msg.message} in date {msg.creation_date} \n'
    return HttpResponse(all_msgs_str)


def create_message(request, sender, reciever, subject, message):
    new_msg = Message()
    new_msg.sender = sender
    new_msg.reciever = reciever
    new_msg.subject = subject
    new_msg.message = message
    new_msg.save()
    return HttpResponse('message sent successfully')


def delete_message(request, email, msg_id):
    msg = Message.objects.get(id=msg_id)
    if msg.sender == email or msg.reciever == email:
        msg.delete()

    return HttpResponse('message deleted successfully')

"""




