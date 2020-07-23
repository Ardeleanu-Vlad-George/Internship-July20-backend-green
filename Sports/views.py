from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from Sports.models import Sports
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from Sports.serializers import SportSerializer


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def sport(request):
    sports = Sports.objects.all()
    serializer = SportSerializer(sports, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)