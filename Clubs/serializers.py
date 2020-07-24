from rest_framework import serializers
from .models import Clubs #ClubUserStatus


#class ClubStatusSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = ClubUserStatus
#        fields = ['user_id']


#class ClubSerializerStatus(serializers.ModelSerializer):
#    pending = ClubStatusSerializer(data=ClubUserStatus.objects.filter(status=0), many=True, read_only=True)
#    requests = ClubStatusSerializer(data=ClubUserStatus.objects.filter(status=1), many=True, read_only=True)
#    members = ClubStatusSerializer(data=ClubUserStatus.objects.filter(status=2), many=True, read_only=True)

#    class Meta:
#        model = Clubs
#        fields = ['__all__', 'pending', 'requests', 'members']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'
