from rest_framework import serializers
from django.contrib.auth.models import User
from . models import President

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = President
        fields = ['id','name', 'party','votes']

