from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('sender', 'reciever', 'subject', 'message', 'creation_date')
        #fields= '__all__'