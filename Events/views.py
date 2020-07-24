from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Events
from user.models import Users
from Events.serializers import EventsSerializer
from user.serializers import UsersSerializer
from rest_framework import permissions, status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from EventsHistory.serilazers import EventsHistorySerializer
from EventsHistory.models import EventsHistory
from django.shortcuts import render

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def events_list(request):
    if request.method == 'GET':
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST', 'DELETE', 'PUT', 'COPY'])
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
        serializeru = UsersSerializer(users, many=True)
        return Response({"event": serializer.data, "users": serializeru.data})
    elif request.method == 'POST':
        Request = EventsHistory(userId=Users.objects.get(id=request.user.id), eventId=Events.objects.get(id=pk))
        Request.save()
        return Response({}, status=200)
    elif request.method == 'COPY': # OPTIONAL
        requests = EventsHistory.objects.all()
        serializer = EventsHistorySerializer(requests, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def get_event_by_user(request, pk):
    if request.method == 'GET':
        user_id = request.user.id
        user_joined_events = EventsHistory.objects.filter(status=EventsHistory.Accepted, user_id=user_id)
        user_joined_events_id = []
        user_pending_events_id = []
        for user in user_joined_events:
            user_joined_events_id.append(user.club_id)
        user_pending_events = EventsHistory.objects.filter(status=EventsHistory.Pending, user_id=user_id)
        for user in user_pending_events:
            user_pending_events_id.append(user.club_id)
        if pk == "joined":
            events = Events.objects.filter(id__in=user_joined_events_id)
            serializer = EventsSerializer(events, many=True)
            return Response(serializer.data)
        elif pk == "pending":
            events = Events.objects.filter(id__in=user_pending_events_id)
            serializer = EventsSerializer(events, many=True)
            return Response(serializer.data)
        elif pk == "unjoined":
            unjoined_events_id = user_pending_events_id + user_joined_events_id
            event = Events.objects.exclude(id__in=unjoined_events_id)
            serializer = EventsSerializer(event, many=True)
            return Response(serializer.data)
        else:
            return Response(status=400)

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def join_event(request, pk):
    token = request.auth
    id = token.user_id
    event = Events.objects.get(id=pk)
    user = Users.objects.get(id=id)
    EventsHistory.objects.create(userId=user, status=EventsHistory.Pending, eventId=event)
    return Response(status=200)

@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def get_events_and_create(request):
    if request.method == "GET":
        event = Events.objects.all()
        serializer = EventsSerializer(event, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = EventsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400)
        if Events.objects.filter(name=request.data.get("name")).exists():
            return Response(status=302)
        serializer.save()
        return Response(status=201)



@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def listing(request, pk, pag):
    if request.method == 'GET':
        eventlist = Events.objects.all()
        paginator = Paginator(eventlist, per_page=pk)
        page_number = pag
        page_obj = paginator.get_page(page_number)
        serializer = EventsSerializer(page_obj, many=True)
        return Response(serializer.data)
