from django.views.generic.base import View  #用listview也可以
from goods.models import Goods
class GoodsListView(View):
    def get(self,request):
        import json
        from django.core import serializers
        from django.http import HttpResponse,JsonResponse
        json_data=serializers.serialize("json",goods)
        json_data=json.loads(json_data)
        # 或者return HttpResponse(json.dumps(json_data), content_type="application/json")
        return JsonResponse(json_data,safe=False)

