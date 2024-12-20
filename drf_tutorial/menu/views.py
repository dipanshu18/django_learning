from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Item
from .serializers import ItemSerializer

def item_list(request: HttpRequest):
    items = Item.objects.all()

    menu_items = []
    
    for item in items:
        menu_items.append({
            "name": item.name,
            "price": item.price,
            "description": item.description
        })

    return JsonResponse({"menu": menu_items})
    

@api_view(["GET"])
def item_list_serialized(request: HttpRequest):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
    
    
@api_view(["GET"])
def item_details(request: HttpRequest, id: int):
    item = Item.objects.get(id=id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)