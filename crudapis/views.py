from rest_framework import generics
from rest_framework.response import Response
from .models import MenuItem
from .serializers import menuItemSerializers , MenuItemModelSerializer

from rest_framework.decorators import api_view
# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemModelSerializer

class MenuItemViewPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = menuItemSerializers