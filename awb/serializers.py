from rest_framework import serializers
from .models import AWB

from kyi_express_user.serializers import Kyi_Express_User_Serializer
from kyi_express_user.models import Kyi_Express_User


class AWBSerializer(serializers.HyperlinkedModelSerializer):
    sender = Kyi_Express_User_Serializer()
    receiver = Kyi_Express_User_Serializer()
        
    
    class Meta:
        model = AWB
        fields = ('awb_number', 'sender', 'receiver')
        

    def create(self, validated_data):
            sender_data = validated_data.pop('sender')
            receiver_data = validated_data.pop('receiver')
            if sender_data:
                sender = Kyi_Express_User.objects.get_or_create(**sender_data)[0]
                validated_data['sender'] = sender
            if receiver_data:
                receiver = Kyi_Express_User.objects.get_or_create(**receiver_data)[0]
                validated_data['receiver'] = receiver
            return AWB.objects.create(**validated_data)