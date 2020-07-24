from rest_framework import serializers
from .models import Events
from Clubs.models import Clubs
from Sports.models import Sports


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


    def update(self, instance, validated_data):
        instance.club = Clubs.objects.get(id=validated_data.get('club', instance.club))
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.radius = validated_data.get('radius', instance.radius)
        instance.location = validated_data.get('location', instance.location)
        instance.sport = Sports.objects.get(id=validated_data.get('sport', instance.sport))
        instance.save()
        return instance
