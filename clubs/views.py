
#std_djngo_libs
from django.shortcuts import render
from rest_framework import permissions
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes

#local_djng_apps
from clubs.serializers import ClubSerializer
from clubs.models import Club


@api_view(['POST'])
@permissions_classes(permissions.IsAuthenticated,)
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
#think it's done, let's test it now