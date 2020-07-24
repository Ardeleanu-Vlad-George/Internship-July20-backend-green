from rest_framework import serializers

from Clubs.models import Clubs
from user.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class GetCoachSerializer(serializers.ModelSerializer):
    clubs = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email', 'age', 'clubs']

    def get_clubs(self, obj):
        return obj.clubs_set.values_list('name', flat=True)

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CoachRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    clubs = serializers.IntegerField()
