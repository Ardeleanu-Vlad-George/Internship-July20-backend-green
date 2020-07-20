from rest_framework.views import APIView
from django.core.mail import BadHeaderError, send_mail
from green.settings import EMAIL_HOST_USER
from .models import Users
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
import random
import string
# Create your views here.


class SendEmail(APIView):

    def reset_password(request):
        to_email = request.POST.get('to_email', '')
        tuple_email = [to_email]
        subject = "New password"
        new_password = get_random_string(10)
        message = "Hello!\n A new password for " + to_email + " has been generated \n The new password is" + new_password
        if to_email:
            try:

                send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
                pass_for_db = make_password(new_password)
                Users.objects.filter(email=to_email).update(password=pass_for_db)
                return HttpResponse(new_password)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    def invite(request):
        to_email = request.POST.get('to_email', '')
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
                pass_for_db = make_password(new_password)


            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

