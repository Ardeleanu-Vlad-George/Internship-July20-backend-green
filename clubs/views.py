from django.shortcuts import render
from clubs.models import Club
from rest_framework import viewsets
from clubs.serialization import ClubSerializer

# Create your views here.

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('-date_joined')
    serializer_class = ClubSerializer
