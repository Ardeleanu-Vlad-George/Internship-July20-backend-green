from rest_framework import serializers
from user import models
from user.models import Users
from .models import Clubs


class ClubsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=30)
    invites = serializers.CharField(max_length=500)
    requests = serializers.CharField(max_length=500)
    members = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return Clubs.objects.create(**validated_data)
