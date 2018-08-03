from rest_framework import serializers
from goods.models import Goods,GoodsCategory

class CategortSerializer3(serializers.ModelSerializer):
    """
    三类
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategortSerializer2(serializers.ModelSerializer):
    """
    二类
    """
    sub_cat=CategortSerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategortSerializer(serializers.ModelSerializer):
    """
    一类
    """
    sub_cat=CategortSerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    category=CategortSerializer()
    class Meta:
        model = Goods
        fields = "__all__"
