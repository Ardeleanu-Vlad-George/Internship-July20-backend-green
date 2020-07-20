from django.shortcuts import render


# Create your views here.

from clubs.models import Club
from rest_framework import viewsets
from clubs.serialization import ClubSerializer

# Create your views here.

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('-id')
    serializer_class = ClubSerializer

