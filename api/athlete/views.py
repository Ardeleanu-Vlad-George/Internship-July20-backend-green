from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticate
from green.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from user.permissions import IsAuthenticate


from user.models import Users
from user.serializers import UsersSerializer, AthleteSerializer
from django.core import serializers

#endpoint for inviting a coach to complete profile and getting all athletes
@csrf_exempt
@api_view(["POST", "GET"])
@permission_classes((IsAuthenticate,))
def athlete(request):
    if request.method == "POST":
        name = request.data.get("name")
        email = request.data.get("email")
        tuple_email = [email]
        subject = "Complete profile"
        message = "Hello coach " + name + "!\nYou have been invited to Sport Management App to complete your profile and set-up password."
        send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
        return HttpResponse(email)
    if request.method == "GET":
        qs = Users.objects.all()
        serializer = AthleteSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

#end-points that allow to get, delete or edit an athlete by id
@csrf_exempt
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes((IsAuthenticate,))
def edit_athlete(request,pk):
    if request.method == 'DELETE':
        athletes = Users.objects.filter(id=request.query_params.get('id', None))
        athletes.delete()
        return JsonResponse([], safe=False)
    elif request.method == 'PUT':
          athletes = Users.objects.get(id=pk)
          serializer = UsersSerializer(athletes, many=False)
          serializer.update(athletes, request.data)
          return JsonResponse({},status=200)
    elif request.method == 'GET':
        athletes = Users.objects.filter(id=request.query_params.get('id', None))
        serializer = UsersSerializer(athletes, many=True)
        return JsonResponse(serializer.data, safe=False)


#end-point for registration
@api_view(['POST'])
@permission_classes((IsAuthenticate,))
def register_athlete(request):
    if request.method == 'POST':
        name = request.data.get("name")
        email = request.data.get("email")
        tuple_email = [email]
        subject = "Complete profile"
        message = "Hello athlete, " + name + "!\nYou have been invited to complete your profile and set up password on Sport Management App"
        if email:
            send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
            return HttpResponse(email)


