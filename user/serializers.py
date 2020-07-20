from rest_framework import serializers
from user.models import Users


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ADMIN = 0
    COACH = 1
    ATHLETE = 2
    ROLES = (
        (0, ADMIN),
        (1, COACH),
        (2, ATHLETE),
    )
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    role = serializers.IntegerField(default=ATHLETE)
    height = serializers.DecimalField(decimal_places=2, max_digits=4)
    weight = serializers.DecimalField(decimal_places=2, max_digits=3)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Users.objects.create(**validated_data)
