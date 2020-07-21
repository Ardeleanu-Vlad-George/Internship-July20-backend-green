from rest_framework import serializers
from user.models import Users


<<<<<<< HEAD
class UserSerializer(serializers.Serializer):
=======
class UsersSerializer(serializers.Serializer):
>>>>>>> 827bf7070bce73d84cc06776d9a40a249405f972
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

<<<<<<< HEAD
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.role = validated_data('role', instance.role)
        instance.height = validated_data('height', instance.height)
        instance.weight = validated_data('weight', instance.weight)
        instance.age = validated_data('age', instance.age)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
=======

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'age']

>>>>>>> 827bf7070bce73d84cc06776d9a40a249405f972
