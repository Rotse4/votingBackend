from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes

from rest_framework import status
from django. contrib.auth.models import User
from rest_framework.response import Response

from account.models import Account
from . serializers import CandidateSerializer
from .models import Candidate
from django.db.models import Q


    
@api_view(['GET'])
def vote(request, pk):
    try:
        candidate = Candidate.objects.get(id=pk)
    except Candidate.DoesNotExist:
        return Response(status=404)  
    
    candidate.votes += 1 
    candidate.save()  
    
    return Response({"name": candidate.account.username,"votes":candidate.votes})


@api_view(['GET'])
def reps(request):
    reps = Candidate.objects.filter(Q(seat="SCHOOL_REP"))
    serializer = CandidateSerializer(reps, many=True)
    return Response({"School reps":serializer.data, "name":"name"})

@api_view(['GET'])
def pesidents(request):
    reps = Candidate.objects.filter(Q(seat="PRESIDENT"))
    serializer = CandidateSerializer(reps, many=True)
    return Response({"Presidents":serializer.data})

@api_view(['GET'])
def wemenRep(request):
    reps = Candidate.objects.filter(Q(seat="WOMENS_REP"))
    serializer = CandidateSerializer(reps, many=True)
    return Response({"Women reps":serializer.data})

@api_view(['GET'])
def menRep(request):
    reps = Candidate.objects.filter(Q(seat="MEN_REP"))
    serializer = CandidateSerializer(reps, many=True)
    return Response({"men reps":serializer.data})