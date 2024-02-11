from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id','ballotName','balotName', 'image','party','votes','description', 'school']

