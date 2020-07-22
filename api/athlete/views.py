from django.core.mail import send_mail
from green.settings import EMAIL_HOST_USER
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from user.models import Users
from user.serializers import UsersSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def athlete(request):
    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')
        subject = 'Complete profile'
        message = 'Hello' + name + ' you have been added as an athlete to Sport Management App'
        tuple_email = [email]
        if email:
            send_mail(subject, message, EMAIL_HOST_USER, tuple_email)
    if request.method == 'GET':
        return JsonResponse({'user': "Gabi"})


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes((permissions.AllowAny,))
def delete_athlete(request):
    if request.method == 'DELETE':
        athletes = Users.objects.filter(id=request.query_params.get('id', None))
        athletes.delete()
        return JsonResponse({}, status=200)
    elif request.method == 'PUT':
        athletes = Users.objects.filter(id=request.query_params.get('id', None))
        serializer = UsersSerializer(athletes, many=False)
        serializer.update(athletes, request.data)
    elif request.method == 'GET':
        athletes = Users.objects.filter(id=request.query_params.get('id', None))
        serializer = UsersSerializer(athletes, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_athlete(request):
    if request.method == 'GET':
        athletes = Users.objects.all()
        serializer = UsersSerializer(athletes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
