from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps.user.models import User


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())],
                                   error_messages={'unique': 'A user with that email already exists.'})

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password'],
            )
            return user
        except IntegrityError as e:
            raise serializers.ValidationError({'email': 'Email address already exists.'})
