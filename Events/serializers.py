from rest_framework import serializers
from user import models
from .models import Events
from user.models import Users

class EventsSerializer(serializers.Serializer):
    club = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=50)
    radius = serializers.CharField(max_length=30)
    location = serializers.CharField(max_length=30)
    def create(self, validated_data):
        return Events.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.club = validated_data.get('club', instance.club)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.radius = validated_data.get('radius', instance.radius)
        instance.location = validated_data('location', instance.location)