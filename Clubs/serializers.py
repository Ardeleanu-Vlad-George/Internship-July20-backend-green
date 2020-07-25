from rest_framework import serializers
from .models import Clubs, ClubUserStatus


class ClubStatusSerializer(serializers.ModelSerializer):
    class Meta:
       model = ClubUserStatus
       fields = ['user_id']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'
