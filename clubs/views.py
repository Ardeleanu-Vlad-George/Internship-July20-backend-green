from django.shortcuts import render
from django.http import HttpResponse

from clubs.models import Club
from clubs.serialization import ClubSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('-id')
    serializer_class = ClubSerializer
