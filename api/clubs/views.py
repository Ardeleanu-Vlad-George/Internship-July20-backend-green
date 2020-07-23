from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from user.models import Users
from Clubs.serializers import ClubSerializerStatus, ClubSerializer
from Clubs.models import Clubs, ClubUserStatus


@csrf_exempt
@api_view(["POST", "GET"])
@permission_classes((AllowAny,))
def club(request):
    if request.method == "POST":

        serializer = ClubSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if Clubs.objects.filter(name=request.data.get("name")).exists():
            return Response(status=status.HTTP_302_FOUND)
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    if request.method == "GET":
        clubs = Clubs.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def club_pk(request, pk):
    if request.method == "GET":
        if not Clubs.objects.filter(id=pk).exists():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        club = Clubs.objects.get(id=pk)
        serializer = ClubSerializer(club, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)



