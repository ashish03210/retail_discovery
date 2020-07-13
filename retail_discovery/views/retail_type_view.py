from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from retail_discovery.models import RetailType
from retail_discovery.serializers import RetailTypeSerializer
from retail_discovery.permissions import RetailDiscoveryAppModelPermission
from retail_discovery.filters import DynamicSearchFilter


class RetailTypeViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = RetailType.objects.all()
    serializer_class = RetailTypeSerializer
    permission_classes = [IsAuthenticated, RetailDiscoveryAppModelPermission]
    filter_backends = (DynamicSearchFilter,)
