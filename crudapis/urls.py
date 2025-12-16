from django.urls import path
from . import views

urlpatterns = [
    path('items', views.MenuIList.as_view()),
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.MenuItemViewPk.as_view()),
    path('filter_items', views.menu_items),
    path('catlist', views.CategouryList.as_view())
]
