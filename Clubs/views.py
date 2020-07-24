from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
<<<<<<< HEAD
=======
from green.permissions import IsCoach, IsAthlete
>>>>>>> 4dc920873052c577dd63e80ebe66c9dfd0bea68c
from user.models import Users
from .models import Clubs, ClubUserStatus
from .serializers import ClubSerializer
from rest_framework import permissions, status
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def get_club_by_user(request, pk):
    if request.method == 'GET':
        user_id = request.user.id
        user_joined_clubs = ClubUserStatus.objects.filter(status=ClubUserStatus.MEMBER, user_id=user_id)
        user_joined_clubs_id = []
        user_pending_clubs_id = []
        for user in user_joined_clubs:
            user_joined_clubs_id.append(user.club_id)
        user_pending_clubs = ClubUserStatus.objects.filter(status=ClubUserStatus.REQUEST, user_id=user_id)
        for user in user_pending_clubs:
            user_pending_clubs_id.append(user.club_id)
        if pk == "joined":
            clubs = Clubs.objects.filter(id__in=user_joined_clubs_id)
            serializer = ClubSerializer(clubs, many=True)
            return Response(serializer.data)
        elif pk == "pending":
            clubs = Clubs.objects.filter(id__in=user_pending_clubs_id)
            serializer = ClubSerializer(clubs, many=True)
            return Response(serializer.data)
        elif pk == "unjoined":
            unjoined_clubs_id = user_pending_clubs_id + user_joined_clubs_id
            clubs = Clubs.objects.exclude(id__in=unjoined_clubs_id)
            serializer = ClubSerializer(clubs, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def join_club(request, pk):
    token = request.auth
    id = token.user_id
    club = Clubs.objects.get(id=pk)
    user = Users.objects.get(id=id)
    ClubUserStatus.objects.create(user=user, status=ClubUserStatus.REQUEST, club=club)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def get_clubs_and_create(request):
    if request.method == "GET":
        clubs = Clubs.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ClubSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if Clubs.objects.filter(name=request.data.get("name")).exists():
            return Response(status=status.HTTP_302_FOUND)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
