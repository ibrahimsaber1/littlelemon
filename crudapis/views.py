from rest_framework import generics
from rest_framework.views import APIView
from .serializers import menuItemSerializers , MenuItemModelSerializer, CategorySerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .models import MenuItem, Category
from rest_framework import status
# Create your views here.
# The line `from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes` is
# importing specific utilities from the `drf_spectacular` package.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemModelSerializer

class MenuItemViewPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = menuItemSerializers

# Create your views here.

@api_view(['GET','POST'])
def menu_items(request):
    #return Response('list of books', status=status.HTTP_200_OK)
    if(request.method=='GET'):
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        serialized_item = menuItemSerializers(items, many=True)
        return Response(serialized_item.data)
    elif request.method=='POST':
        serialized_item = menuItemSerializers(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data,status.HTTP_201_CREATED)


class CategouryList(APIView):
    @extend_schema(
                parameters=[
            OpenApiParameter(name='slug', description='Filter by artist', required=True, type=OpenApiTypes.STR),
            OpenApiParameter(name='title', type=OpenApiTypes.INT, description='Filter by release year'),
        ],
        responses={201: CategorySerializer}
    )
    def get(self, request):
        cat_model = Category.objects.all()
        cat_serializer = CategorySerializer(cat_model)
        return Response(cat_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        cat_serializer = CategorySerializer(request.data)
        if cat_serializer.is_valid():
            cat_serializer.save()
            return Response(cat_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        