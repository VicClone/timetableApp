from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
        Сериализатор для пользователя
    """
    class Meta:
        model = User
        fields = ('pk', 'login', 'email', 'first_name', 'last_name')