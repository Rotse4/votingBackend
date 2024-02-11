from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes

# Create your views here.
from rest_framework import status
from django. contrib.auth.models import User
from rest_framework.response import Response
from . serializers import RegistrationSerializer
from .models import Candidate


    
@api_view(['GET'])
def vote(request, pk):
    try:
        candidate = Candidate.objects.get(id=pk)
    except Candidate.DoesNotExist:
        return Response(status=404)  # Return a 404 response if candidate doesn't exist
    
    candidate.votes += 1  # Increase votes by 2
    candidate.save()  # Save the changes to the existing Candidate object
    
    return Response({"name": candidate.name.username,"votes":candidate.votes})




