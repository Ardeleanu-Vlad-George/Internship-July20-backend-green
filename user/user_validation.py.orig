from .rest_framework import serializers
from user.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'role',
            'height',
            'weight',
            'age'
        )

        def clean_first(self):
            if self.first_name == '':
                raise ValidationError('Empty field')
            if len(self.first_name) > 30:
                raise ValidationError('Enter a correct first name')

        def clean_second(self):
            if self.last_name == '':
                raise ValidationError('Empty field')
            if len(self.last_name) > 30:
                raise ValidationError('Enter a correct first name')

        def clean_email(self):
            if self.email == '':
                raise ValidationError('Empty field')
            if not validate_email(self.email):
                raise ValidationError('Enter a correct email')

        def clean_role(self):
            if self.role is None:
                raise ValidationError('Empty field')
            if self.role < 0 or self.role.isdigit() is False:
                raise ValidationError('Enter a valid role')

        def clean_age(self):
            if self.age is None:
                raise ValidationError('Empty field')
            if self.age < 0 or self.age > 99 or self.age.isdigit() is False:
                raise ValidationError('Enter a valid age')

        def clean_height(self):
            if self.height is None:
                raise ValidationError('Empty field')
            if self.height < 0 or self.height > 2.5 or self.role.isdigit() is False:
                raise ValidationError('Enter a valid height')

        def clean_weight(self):
            if self.weight is None:
                raise ValidationError('Empty field')
            if self.weight < 0 or self.weight > 150:
                raise ValidationError('Enter a valid weight')
