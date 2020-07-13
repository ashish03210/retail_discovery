from rest_framework import serializers
from django.contrib.auth.models import Group

from r_auth.serializers import PermissionSerializer, GroupPermissionSerializer


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')
        extra_kwargs = {'permissions': {'write_only': True}}

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)
        group = Group(**validated_data)
        group.save()
        if permissions and len(permissions) > 0:
            group.permissions.set(permissions)
        return group

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        if validated_data.get('permissions') and len(validated_data.get('permissions')) > 0:
            instance.permissions.set(validated_data.get('permissions'))

        return instance


class GroupListSerializer(serializers.ModelSerializer):
    permissions = GroupPermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')
        extra_kwargs = {'permissions': {'read_only': True}}


class EmployeeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)
