from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item 
from .serializer import ItemSerializer
# Create your views here.


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serial = ItemSerializer(items, many=True)
    return Response(serial.data)

@api_view(['POST'])
def addItem(request):
    serial = ItemSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)