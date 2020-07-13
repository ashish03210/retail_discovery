from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import Group

from r_auth.models import User
from r_auth.serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    @action(detail=False)
    def groups(self, request):
        ug_qs = Group.objects.filter(user=request.user)
        user_groups = [g.name for g in ug_qs]
        return Response(user_groups)
