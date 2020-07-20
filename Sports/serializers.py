from rest_framework import serializers
from .models import Sports

class SportSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Running = 0
    Cicling = 1
    TeamSports = 2
    WeightLifting = 3
    TYPES = (
        (0, Running),
        (1, Cicling),
        (2, TeamSports),
        (3, WeightLifting),
    )
    type = serializers.IntegerField(default=Running, choices=TYPES)
    def create(self, validated_data):
        return Sports.objects.create(**validated_data)