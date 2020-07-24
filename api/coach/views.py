from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, serializers
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from Clubs.models import Clubs
from Clubs.serializers import ClubSerializer
from green.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
from user.models import Users
from user.views import get_random_string
from user.serializers import GetCoachSerializer, CoachRegistrationSerializer, CoachSerializer


@csrf_exempt
@api_view(["POST", "GET", "PUT"])
@permission_classes((AllowAny,))
def coach(request):
    if request.method == "POST":
        serializer = CoachRegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        email = serializer.data.get("email")
        if Users.objects.filter(email=email).exists():
            return Response(status=status.HTTP_302_FOUND)
        Users.objects.create(email=email, role=Users.COACH, first_name=serializer.data.get("first_name"),
                             last_name=serializer.data.get("last_name")
                             )
        tuple_email = [email]
        name = serializer.data.get("first_name") + " " + serializer.data.get("last_name")
        password = get_random_string(10)
        password_for_db = make_password(password)
        Users.objects.filter(email=email).update(password=password_for_db)
        coach_id = Users.objects.get(email=email).id
        Clubs.objects.filter(id=serializer.data.get("clubs")).update(owner_id=coach_id)
        subject = "Complete profile"
        message = "Hello, " + name + "\n You have been added as a coach to Sport Management App."
        message = message + "\nYour password is " + password
        send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
        return Response(status=status.HTTP_202_ACCEPTED)
    if request.method == "PUT":
        coach = Users.objects.get(id=request.data.get("id"))
        serializer = CoachSerializer(coach)
        serializer.update(serializer.instance, request.data)
        Clubs.objects.filter(id=request.data.get("clubs")).update(owner_id=coach.id)
        return Response(status=status.HTTP_202_ACCEPTED)

    if request.method == "GET":
        coaches = Users.objects.filter(role=Users.COACH)
        serializer = GetCoachSerializer(coaches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "DELETE"])
@permission_classes((AllowAny,))
def coach_pk(request, pk):
    if request.method == "GET":
        if not Users.objects.filter(id=pk).exists():
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        coach = Users.objects.get(id=pk)
        serializer = GetCoachSerializer(coach, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        if not Users.objects.filter(id=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        coach = Users.objects.get(id=pk)
        coach.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_coach_clubs(request, pk):
    if not Clubs.objects.filter(owner=pk).exists():
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    club = Clubs.objects.filter(owner=pk)
    serializer = ClubSerializer(club, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#ptr IMAGINI FOLOSESTI TEXT FIELD IMaginea este in base64



