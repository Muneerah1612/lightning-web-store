from django.urls import path
from .views import ProductListView, AddProductView, CreateCategoryView, CreateCartItemView, CartSummaryView, CheckoutView

urlpatterns=[
    path('category/', CreateCategoryView.as_view(), name='category'),
    path('addproduct/',AddProductView.as_view(),name='product'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('add_to_cart/', CreateCartItemView.as_view(), name='cart_item'),
    path('cart_price/', CartSummaryView.as_view(), name='cart_price'),
    path('checkout/<int:cart_id>/', CheckoutView.as_view(), name='checkout'),
]