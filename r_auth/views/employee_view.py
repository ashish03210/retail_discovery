from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from r_auth.models import User
from r_auth.serializers import EmployeeSerializer, UserSerializer
from retail_discovery.filters import DynamicSearchFilter


class EmployeeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_class_override = {
        'list': EmployeeSerializer,
        'retrieve': EmployeeSerializer,
    }
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = (DynamicSearchFilter, DjangoFilterBackend)
    filter_fields = ['groups']

    def get_serializer_class(self):
        return self.serializer_class_override.get(self.action, self.serializer_class)
