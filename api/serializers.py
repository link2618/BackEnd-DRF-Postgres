from rest_framework import serializers
from .models import User, Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'lastName', 'date', 'email', 'password', 'tipo')
        extra_kwargs = {'password': {'write_only': True}}

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('__all__')
