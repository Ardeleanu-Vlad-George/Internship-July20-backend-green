from rest_framework.views import APIView
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


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def reset_password(request):
    to_email = request.data.get("to_email")
    tuple_email = [to_email]
    subject = "New password"
    new_password = get_random_string(10)
    message = "Hello!\n A new password for " + to_email + " has been generated \n The new password is" + new_password
    if to_email:
        try:

            send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
            pass_for_db = make_password(new_password)
            Users.objects.filter(email=to_email).update(password=pass_for_db)
            return Response(status=status.HTTP_200_OK)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')


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


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def registration(request):
    name_input = request.data.get("first_and_last_name")
    first = name_input.split()[0]
    last = name_input.split()[1]
    register_email = request.data.get("email")
    password = request.data.get("password")
    confirm_password = request.data.get("confirm_password")
    if password != confirm_password:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    pass_for_db = make_password(confirm_password)
    if Users.objects.filter(email=register_email).exists():
        return Response(status=status.HTTP_204_NO_CONTENT)
    Users.objects.create(first_name=first, last_name=last, email=register_email, password=pass_for_db)
    return Response(status=status.HTTP_201_CREATED)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
