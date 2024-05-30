from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item 
from .serializer import ItemSeriealizer
# Create your views here.


@api_view(['GET'])
def items(request):
    all_items = Item.objects.all()
    serial = ItemSeriealizer(all_items, many=True)
    return Response(serial.data)
@api_view(['POST'])
def addItem(request):
    serial = ItemSeriealizer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)