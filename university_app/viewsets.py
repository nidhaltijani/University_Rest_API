from .models import *
from rest_framework import viewsets 
from .serializers import *
class studentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=studentSerializer
    http_method_name=["get","post","put","delete"]
    
class groupViewset(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=groupeSerializer
    http_method_name=["get","post","put","delete"]
    
class addressViewset(viewsets.ModelViewSet):
    queryset=address.objects.all()
    serializer_class=addressSerializer
    http_method_name=["get","post","put","delete"]