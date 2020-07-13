from rest_framework import filters as drf_filters
from django_filters import rest_framework as filters
import django_filters


class DynamicSearchFilter(drf_filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])