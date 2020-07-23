from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from Clubs.models import Clubs
from green.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
from user.models import Users
from django.core import serializers
from user.serializers import GetCoachSerializer, CoachRegistrationSerializer


@csrf_exempt
@api_view(["POST", "GET"])
@permission_classes((AllowAny,))
def coach(request):
    if request.method == "POST":
        serializer = CoachRegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        email = serializer.data.get("email")
        if Users.objects.filter(email=email).exists():
            return Response(status=status.HTTP_302_FOUND)
        tuple_email = [email]
        subject = "Complete profile"
        message = "Hello, " + serializer.data.get("name") + "\n You have been added as a coach to Sport Management App"
        send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
        return Response(status=status.HTTP_202_ACCEPTED)
    if request.method == "GET":
        clubs = Clubs.objects.all()
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



