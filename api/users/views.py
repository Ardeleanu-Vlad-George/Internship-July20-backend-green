
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from green.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse

from user.models import Users
from user.serializers import UsersSerializer
from django.core import serializers
from user.serializers import CoachSerializer

@csrf_exempt
@api_view(["POST", "GET"])
@permission_classes((AllowAny,))
def coach(request):
    if request.method == "POST":
        name = request.data.get("name")
        email = request.data.get("email")
        tuple_email = [email]
        subject = "Complete profile"
        message = "Hello, " + name + "\n You have been added as a coach to Sport Management App"
        if email:
            send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
            return HttpResponse(email)
    if request.method == "GET":
        qs = Users.objects.all()
        serializer = CoachSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)




