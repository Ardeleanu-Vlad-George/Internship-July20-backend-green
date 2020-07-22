
#std_djngo_libs
from django.shortcuts import render
from rest_framework import permissions
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes


#local_djng_apps
from clubs.serializers import ClubSerializer
from clubs.models import Club

#import datetime

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def all_clubs(request):
    qry_rspns = Club.objects.all().count()
    if qry_rspns:
        return JsonResponse({"nr of clubs": qry_rspns})
    else:
        return JsonResponse({"clubs exist?": False})

@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def new_club(request):
    serializer = ClubSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return JsonResponse(serializer.data)
        except IntegrityError as already_exists:
            alrd_clb = Club.objects.filter(name=serializer.name)
            return JsonResponse(ClubSerializer(alrd_clb))
    return JsonResponse(serializer.errors, status=400)


