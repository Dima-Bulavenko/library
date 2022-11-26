from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'first_name', 'last_name', 'middle_name', 'email', 'role', 'password', 'created_at',
                  'updated_at', 'is_superuser', 'is_staff', 'is_active']
