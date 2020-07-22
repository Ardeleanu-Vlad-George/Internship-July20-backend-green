
from django.shortcuts import render
from .models import Events
from Events.serializers import EventsSerializer
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def events_list(request):
    if request.method == 'GET':
        events = Events.objects.all()
        serializer = EventsSerializer(events, status=201)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)