from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Candidate

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','name', 'party','votes','description', 'school']

