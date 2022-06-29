from rest_framework import serializers
from .models import Category, Product, Cart, Payment, CartItem


class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
