
#my_app
from clubs.models import Club
from clubs.serialization import ClubSerializer
#from clubs.forms import ClubForm

#std_libs
from rest_framework import viewsets
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
'''

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('-id')
    serializer_class = ClubSerializer

