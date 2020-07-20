from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from green.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse


class CoachView(APIView):
    @csrf_exempt
    @api_view(["POST","GET"])
    @permission_classes((AllowAny,))
    def coach(request):
        if request.method == "POST":
            name = request.data.get("name")
            email = request.data.get("email")
            tuple_email=[email]
            subject = "Complete profile"
            message = "Hello, " + name + "\n You have been added as a coach to Sport Management App"
            if email:
                send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
                return HttpResponse(email)


        if request.method == "GET":

            return JsonResponse({"user": "mihai",})
