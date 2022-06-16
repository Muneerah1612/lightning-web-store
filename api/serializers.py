from rest_framework import serializers
from .models import Category,Product, Cart,Payment


class AddCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

