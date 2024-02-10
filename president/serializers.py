from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Candidate, Voter

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','name', 'party','votes','description', 'school']

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Voter
        fields= ['id','name','regNo','voted']
