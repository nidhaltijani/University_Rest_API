from rest_framework import serializers
from .models import *
class studentSerializer(serializers.ModelSerializer):
    class Meta():
        model=Student 
        fields='__all__'
        
class groupeSerializer(serializers.ModelSerializer):
    class Meta():
        model=Group
        fields='__all__'
        
class addressSerializer(serializers.ModelSerializer):
    class Meta():
        model=address 
        fields='__all__'
