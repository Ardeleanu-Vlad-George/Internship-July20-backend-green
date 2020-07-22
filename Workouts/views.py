from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from user.models import Users
from rest_framework import serializers
from django.http import JsonResponse
from Workouts.serializers import WorkoutSerializer
from .models import Workouts
# class WorkoutsViewSet(viewsets.ViewSet):
#    queryset = Users.objects.all()
#
#    @action(detail=True, methods=['post'], name='Set Workout')
#    def set_workout(self, request, pk=None):
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    @action(detail=True, methods=['get'], name='Workout History')
#    def workout_history(self, request, pk=None):
#        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def workout_list(request):
    if request.method == 'GET':
        workouts = Workouts.objects.filter(owner=request.user.id)
        serializer = WorkoutSerializer(workouts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Create your views here.
