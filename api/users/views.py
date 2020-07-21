from django.core.mail import send_mail
from django.shortcuts import render
from requests import Response

from green.settings import EMAIL_HOST_USER

from Events.serializers import EventsSerializer
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView







