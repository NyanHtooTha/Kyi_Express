
from .models import AWB
from .serializers import AWBSerializer

from rest_framework import viewsets

# Create your views here.


class AWBViewSet(viewsets.ModelViewSet):
    queryset = AWB.objects.all()
    serializer_class = AWBSerializer
    
    def get_view_name(self):
        super(AWBViewSet, self).get_view_name()
        return "AWB List"
        