from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'first_name', 'last_name', 'middle_name', 'email', 'role', 'password', 'created_at',
                  'updated_at', 'is_superuser', 'is_staff', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        role = validated_data.pop('role')
        first_name = validated_data.pop('first_name')
        middle_name = validated_data.pop('middle_name')
        last_name = validated_data.pop('last_name')
        return CustomUser.create(email=email, password=password, role=role, first_name=first_name,
                                 middle_name=middle_name, last_name=last_name)

    def update(self, instance, validated_data):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        middle_name = self.validated_data['middle_name']
        password = self.validated_data['password']
        role = self.validated_data['role']
        instance.update(first_name=first_name,
                        last_name=last_name,
                        middle_name=middle_name,
                        password=password,
                        role=role,
                        )

        return instance
