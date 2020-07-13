from rest_framework import serializers

from r_auth.models import User
from r_auth.serializers import EmployeeGroupSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'email', 'is_staff', 'first_name', 'last_name', 'password', 'username', 'groups')
        extra_kwargs = {'password': {'write_only': True}, 'url': {'read_only': True}, 'groups': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        groups = validated_data.pop('groups', None)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        if groups and len(groups) > 0:
            user.groups.set(groups)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_staff = validated_data.get('is_staff', instance.last_name)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()

        if validated_data.get('groups') and len(validated_data.get('groups')) > 0:
            instance.groups.set(validated_data.get('groups'))

        return instance


class EmployeeSerializer(serializers.ModelSerializer):
    groups = EmployeeGroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff', 'groups', 'first_name', 'last_name', 'date_joined')
        extra_kwargs = {'groups': {'read_only': True}}
