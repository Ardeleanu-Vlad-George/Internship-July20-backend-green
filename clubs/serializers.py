
from rest_framework import serializers
from clubs.models import Club, ClubHistory

class ClubSerializer(serializers):
    name = serializers.CharField(200)
    description = serializers.CharField(400)

    def create(self, validated_input):
        return Club.objects.create(**validated_input)

    def update(self, instance, validated_input):
        instance.name = validated_input.get('name', instance.name)
        instance.description = validated_input.get('description', instance.description)
