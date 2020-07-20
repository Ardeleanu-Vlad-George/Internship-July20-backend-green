from rest_framework import serializers
from Workouts.models import Workouts
from user.models import Users
from user.serializers import UserSerializer
from Sports.models import Sports

class WorkoutSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=50)
    lat = serializers.DecimalField(decimal_places=2, max_digits=4)
    lng = serializers.DecimalField(decimal_places=2, max_digits=4)
    radius = serializers.DecimalField(decimal_places=2, max_digits=4)
    duration = serializers.DecimalField(decimal_places=2, max_digits=4)
    distance = serializers.DecimalField(decimal_places=2, max_digits=4)
    average_hr = serializers.DecimalField(decimal_places=2, max_digits=4)
    calories_burned = serializers.DecimalField(decimal_places=2, max_digits=4)
    average_speed = serializers.DecimalField(decimal_places=2, max_digits=4)
    workout_effectiveness = serializers.BooleanField()
    def create(self, validated_data):
        return Workouts.objects.create(**validated_data)