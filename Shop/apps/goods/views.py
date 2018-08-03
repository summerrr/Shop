from .serializers import GoodsSerializer,CategortSerializer
from rest_framework import mixins

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods,GoodsCategory
from .filters import GoodsFilter

class GoodsPagination(PageNumberPagination):
    page_size=12  #每页12条
    page_size_query_param='page_size'
    page_query_param = "page"#名字
    max_page_size = 100

# class GoodsListView(generics.ListAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
     商品列表页，搜索、分页、排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination


    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class=GoodsFilter
    search_fields =('name','goods_brief','goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

class CategoryViewset(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    """
    List:
        商品分类列表数据,只需加mixins.RetrieveModelMixin就能进入详情页
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategortSerializer