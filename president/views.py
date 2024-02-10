from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes

# Create your views here.
from rest_framework import status
from django. contrib.auth.models import User
from rest_framework.response import Response
from . serializers import RegistrationSerializer, VoterSerializer
from .models import Candidate,Voter



# @api_view(['POST'])
# def registration(request):
#     print(request.data)
#     name = request.data.get('name')
#     print(name)
#     serializer = RegistrationSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         # print(presidentD.name)
#         return Response(serializer.data)
#     else:
#         print("shenzi")

#         return Response( serializer.errors)
    


@api_view(['POST'])
def registration(request):
    print(request.data)
    name = request.data.get('name')
    print(name)
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # print(presidentD.name)
        return Response(serializer.data)
    else:
        print("shenzi")

        return Response( serializer.errors)
    
@api_view(['GET'])
def vote(request, pk):
    try:
        candidate = Candidate.objects.get(id=pk)
    except Candidate.DoesNotExist:
        return Response(status=404)  # Return a 404 response if candidate doesn't exist
    
    candidate.votes += 1  # Increase votes by 2
    candidate.save()  # Save the changes to the existing Candidate object
    
    return Response(candidate.votes)


@api_view(['POST'])
def register_voter(request):
    serializer = VoterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("h")
        return Response(serializer.data)
    print("from errors")
    return Response(serializer.errors)
    
# class Candidate(models.Model):
#     name = models.CharField(max_length=200)
#     party =models.CharField(max_length= 100,choices=parties, default="Independent")
#     seat = models.CharField(max_length=200)
#     school =models.CharField(max_length=200)
#     description = models.TextField()
#     votes=models.IntegerField(default=0)
    
    

