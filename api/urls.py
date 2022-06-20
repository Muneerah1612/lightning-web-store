from django.urls import path
from .views import ProductListView, AddProductView, CreateCategoryView

urlpatterns=[
    path('category/', CreateCategoryView.as_view(), name='category'),
    path('addproduct/',AddProductView.as_view(),name='product'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
]