from django.shortcuts import render
from .models import Events
from user.models import Users
from Events.serializers import EventsSerializer
from user.serializers import UserSerializer
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from EventsHistory.serilazers import EventsHistorySerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def events_list(request):
    if request.method == 'GET':
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes((permissions.AllowAny,))
def delete_event(request, pk):
    if request.method == 'DELETE':
        events = Events.objects.filter(id=pk)
        events.delete()
        return JsonResponse({}, status=200)
    elif request.method == 'PUT':
        events = Events.objects.get(id=pk)
        serializer = EventsSerializer(events, many=False)
        serializer.update(serializer.instance, request.data)
        return JsonResponse({}, status=200)
    elif request.method == 'GET':
        events = Events.objects.filter(id=pk)
        serializer = EventsSerializer(events, many=True)
        users = Users.objects.filter(id=events.members)
        serializeru = UserSerializer(users, many=True)
        return Response({"event": serializer.data, "users": serializeru.data})
    elif request.method == 'POST':
        serializer = EventsHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

