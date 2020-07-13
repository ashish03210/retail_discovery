from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import Group

from r_auth.serializers import GroupSerializer, GroupListSerializer


class GroupViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    serializer_class_override = {
        'list': GroupListSerializer,
        'retrieve': GroupListSerializer,
    }
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = None

    def get_serializer_class(self):
        return self.serializer_class_override.get(self.action, self.serializer_class)
