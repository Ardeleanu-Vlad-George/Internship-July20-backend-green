
from rest_framework import serializers
from clubs.models import Club, ClubHistory

class ClubSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=400)

    def create(self, validated_input):
        return Club.objects.create(**validated_input)
