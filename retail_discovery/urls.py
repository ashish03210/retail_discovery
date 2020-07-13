from rest_framework import routers
from django.urls import path

from retail_discovery.views import RetailTypeViewSet

router = routers.DefaultRouter()
router.register(r'retail_type', RetailTypeViewSet)
