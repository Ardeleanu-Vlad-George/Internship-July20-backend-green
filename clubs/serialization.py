from clubs.models import Club #, Event
from rest_framework import serializers


#to make serializers

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'owner', 'name', 'description']



"""
class EventSerializer(serializers.Serializer):
    class Meta:
"""