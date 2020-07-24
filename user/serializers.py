from rest_framework import serializers

from Clubs.models import Clubs
from Sports.models import Sports
from user.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.primary_sport = Sports.objects.get(id=validated_data.get('primary_sport', instance.club))
        instance.secondary_sport = Sports.objects.get(id=validated_data.get('secondary_sport', instance.club))
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.height)
        instance.age = validated_data.get('age', instance.height)
        instance.save()
        return instance


class GetCoachSerializer(serializers.ModelSerializer):
    clubs = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email', 'clubs']

    def get_clubs(self, obj):
        return obj.clubs_set.values_list('name', flat=True)


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CoachRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    clubs = serializers.IntegerField()
