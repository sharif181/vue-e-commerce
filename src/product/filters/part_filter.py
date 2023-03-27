from django_filters import rest_framework as filters
from product.models.product_models import Part
import django_filters


class PartFilter(filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Part
        fields = '__all__'


class PartExactTitleFilter(filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='exact')

    class Meta:
        model = Part
        fields = '__all__'
