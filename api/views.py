from django.shortcuts import render
from rest_framework import status
from .serializers import AddCategorySerializer, AddProductSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Product, Cart,Category, Payment


# AddtoCart (addproductstocart)
# CartList (getaparticularcartlist)
# Checkout() 
# Payment 
# PaymentConfirmation 
class CreateCategoryView(APIView):
    permission_classes = [AllowAny]
    """ this allows user to create category"""

    def post(self, request):
        data = request.data
        serializer = AddCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED,
                             'message': 'Category has been successfully created'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})

class AddProductView(APIView):
    permission_classes = [AllowAny]
    """ this allows user to add product"""

    def post(self, request):
        data = request.data
        serializer = AddProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED,
                             'message': 'Product has been successfully added'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})

class ProductListView(APIView):
    permission_classes = [AllowAny]
    """ to get all products """

    def get(self, request, format=None):
        """ Return a list of all products."""
        products = Product.objects.all()
        serializer = AddProductSerializer(products, many=True)
        return Response(serializer.data)



