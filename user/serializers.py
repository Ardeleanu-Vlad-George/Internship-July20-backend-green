from rest_framework import serializers
from user.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class GetCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email', 'age']


class RequestCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CoachRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
