from rest_framework import serializers
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
