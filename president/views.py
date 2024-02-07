from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes

# Create your views here.
from rest_framework import status
from django. contrib.auth.models import User
from rest_framework.response import Response
from . serializers import RegistrationSerializer
from .models import Candidate



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
def vote(request,pk):
    candidate = Candidate.objects.get(id=pk)
    serializer =RegistrationSerializer(data=candidate,)
    candidate.votes+=1
    if serializer.is_valid():
        serializer.save
    else:
        print("imekataa")
    return Response({"candidate": serializer.data})

    
