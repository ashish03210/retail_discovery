from django.conf.urls import url, include
from rest_framework import routers
from r_auth.views import UserViewSet, EmployeeViewSet, PermissionViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'group', GroupViewSet)
