import django_filters
from .models import Goods
from django.db.models import Q

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(field_name='shop_price',lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
   # name=django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    top_category=django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self,queryset,name,value):
        """
        查找第一类别所对应的商品
        :param queryset:
        :param name:
        :param value:
        :return:
        """
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)
                                 |Q(category__parent_category__parent_category_id=value))
    class Meta:
        model = Goods
        fields = ['pricemin','pricemax']
