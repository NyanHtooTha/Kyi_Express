from rest_framework import serializers
from .models import AWB

from kyi_express_user.serializers import Kyi_Express_User_Serializer


class AWBSerializer(serializers.HyperlinkedModelSerializer):
    sender = Kyi_Express_User_Serializer()
    receiver = Kyi_Express_User_Serializer()
        
    
    class Meta:
        model = AWB
        fields = ('awb_number', 'sender', 'receiver')
        

    def create(self, validated_data):
            sender_data = validated_data['sender']
            receiver_data = validated_data['receiver']
            if sender_data:
                sender_serializer = Kyi_Express_User_Serializer(data=sender_data)
                if sender_serializer.is_valid():
                    sender_id = sender_serializer.save()
                validated_data['sender'] = sender_id
            if receiver_data:
                receiver_serializer = Kyi_Express_User_Serializer(data=receiver_data)
                if receiver_serializer.is_valid():
                    receiver_id = receiver_serializer.save()
                validated_data['receiver'] = receiver_id
            return AWB.objects.create(**validated_data)