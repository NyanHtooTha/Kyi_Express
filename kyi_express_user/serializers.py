
from rest_framework import serializers
from .models import Kyi_Express_User



class Kyi_Express_User_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Kyi_Express_User
        fields = ("name", "mobile", "address")