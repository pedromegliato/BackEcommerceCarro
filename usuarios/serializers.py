from dataclasses import fields
from rest_framework import serializers
from usuarios.models import User


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            'password',
            'date_joined',
            'groups',
            'user_permissions'
        )
