from rest_framework import serializers
from .models import EventsHistory


class EventsHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsHistory
        fields = ['id', 'userId', 'status', 'eventId']
