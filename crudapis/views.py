from rest_framework import generics
from rest_framework.views import APIView
from .serializers import menuItemSerializers , MenuItemModelSerializer, MenuItemModelSerializerCreate ,CategorySerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .models import MenuItem, Category
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
# The line `from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes` is
# importing specific utilities from the `drf_spectacular` package.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemModelSerializer

class MenuItemViewPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemModelSerializer

# Create your views here.

@api_view(['GET','POST'])
def menu_items(request):
    #return Response('list of books', status=status.HTTP_200_OK)
    if(request.method=='GET'):
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        #pagination
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__startswith=search) # if i want to search if the word starts with this keyword. 
            # items = items.filter(title__contains=search)  # use this if u want to search for the keyword in any part of the title
            #NOTE: the above search is case sensitive if u want to make it case insensitive use i before startswith or contains for example >> title__istartswith or title__icontains
        if ordering:
            items= items.order_by(ordering)        
            
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
            
        serialized_item = MenuItemModelSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method=='POST':
        serialized_item = MenuItemModelSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data,status.HTTP_201_CREATED)

# USES API VIEW on menus

class MenuIList(APIView):
    def get(self, request):
        cat_model = MenuItem.objects.all()
        cat_serializer = MenuItemModelSerializer(cat_model, many=True)
        return Response(data=cat_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        cat_serializer = MenuItemModelSerializerCreate(data=request.data)
        if cat_serializer.is_valid():
            cat_serializer.save()
            return Response(cat_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        


class CategouryList(APIView):
    def get(self, request):
        cat_model = Category.objects.all()
        cat_serializer = CategorySerializer(cat_model, many=True)
        return Response(data=cat_serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
                parameters=[
            OpenApiParameter(name='slug'    ),
            OpenApiParameter(name='title'),
        ],
        responses={201: CategorySerializer}
    )
    def post(self, request):
        cat_serializer = CategorySerializer(data=request.data)
        if cat_serializer.is_valid():
            cat_serializer.save()
            return Response(cat_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        