from rest_framework import serializers
from .models import *
"""
for wiewsets
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
""" 
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__' #serializes all fields
        #fields=('id','name','familyName','group') #serializes only these fields
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__' #serializes all fields
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= address
        fields='__all__' #serializes all fields
        
