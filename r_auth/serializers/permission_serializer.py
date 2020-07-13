from rest_framework import serializers
from django.contrib.auth.models import Permission

from r_auth.serializers import ContentTypeSerializer


class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer()

    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename', 'content_type',)
        extra_kwargs = {'content_type': {'read_only': True}}


class GroupPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename',)
