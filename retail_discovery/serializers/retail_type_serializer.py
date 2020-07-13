from rest_framework import serializers

from retail_discovery.models import RetailType


class RetailTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailType
        fields = ('id', 'name',)
