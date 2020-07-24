from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from user.models import Users
from Clubs.serializers import ClubSerializer
from Clubs.models import Clubs



@csrf_exempt
@api_view(["GET", "DELETE"])
@permission_classes((AllowAny,))
def club_pk(request, pk):
    if request.method == "DELETE":
        if not Clubs.objects.filter(id=pk).exists():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        club = Clubs.objects.get(id=pk)
        club.delete()
        return Response(status=status.HTTP_200_OK)
    if request.method == "GET":
        if not Clubs.objects.filter(id=pk).exists():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        club = Clubs.objects.get(id=pk)
        serializer = ClubSerializer(club, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)





