from django.core.mail import BadHeaderError, send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from green.settings import EMAIL_HOST_USER
from .models import Users
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
import random
import string
# Create your views here.
from .serializers import EmailSerializer
from .serializers import UsersSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def registration(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        db_password = make_password(serializer.data.get("password"))
        Users.objects.filter(email=serializer.data.get("email")).update(password=db_password)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def update_profile(request):
    athlete = Users.objects.get(id=request.data.get("id"))
    serializer = UsersSerializer(athlete, many=False)
    serializer.update(serializer.instance, request.data)
    return Response(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def reset_password(request):
    serializer = EmailSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    to_email = serializer.data.get("email")
    if not Users.objects.filter(email=to_email).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    tuple_email = [to_email]
    subject = "New password"
    new_password = get_random_string(10)
    message = "Hello!\n A new password for " + to_email + " has been generated \n The new password is" + new_password
    send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
    pass_for_db = make_password(new_password)
    Users.objects.filter(email=to_email).update(password=pass_for_db)
    return Response(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def invite(request):
    to_email = request.data.get("to_email")
    tuple_email = [to_email]
    subject = "Invitation"
    new_password = get_random_string(10)
    message = "Hello!\nYou have been invited to Sport Management App  \n The password is" + new_password
    if to_email:
        try:
            exist = Users.objects.filter(email=to_email).exists()
            if exist:
                return HttpResponse({'User already exists'})
            send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
    return HttpResponse(status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def check_email(request):
    serializer = EmailSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    new_email = serializer.data.get("email")
    if Users.objects.filter(email=new_email).exists():
        return Response(status=status.HTTP_302_FOUND)
    return Response(status=status.HTTP_202_ACCEPTED)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
