from django.shortcuts import render
from .models import Clubs
from .serializers import ClubsSerializer
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def clubs_list(request):
    if request.method == 'GET':
        clubs = Clubs.objects.all()
        serializer = ClubsSerializer(clubs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = ClubsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# Create your views here.
