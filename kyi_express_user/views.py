from .models import Kyi_Express_User
from .serializers import Kyi_Express_User_Serializer

from rest_framework import viewsets
# Create your views here.


class Kyi_Express_User_ViewSet(viewsets.ModelViewSet):
    queryset = Kyi_Express_User.objects.all()
    serializer_class = Kyi_Express_User_Serializer
