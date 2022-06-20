from django.shortcuts import render
from rest_framework import status
from .serializers import AddCategorySerializer, AddProductSerializer, CartItemSerializer, CartSummarySerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Product, Cart,Category, Payment, CartItem


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

class CreateCartItemView(APIView):
    def post(self,request):
        data=request.data
        serializer=CartItemSerializer(data=data)
        cart_item=request.data['product']
        quantity=request.data['quantity']
        product=Product.objects.get(name=cart_item)

        if product.stock < int(quantity):
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message':f'Item is less than {quantity}'
                }
            )
        else:
            new_stock=product.stock - int(quantity)
            Product.objects.filter(name=cart_item).update(stock=int(new_stock))
            if serializer.is_valid():
                
                serializer.save()
            
            pr=CartItem.objects.get(user=request.user.id)
            print(pr)

                
            return Response(
                {
                    'status':status.HTTP_201_CREATED,
                    'data':serializer.data,
                    
                    
                }
            )

class CartSummaryView(APIView):
    def get(self,request):
        user_id=request.user.id
        

        user = User.objects.get(id=user_id)
        items=CartItem.objects.filter(user=user_id).all()
        
        total=0
        description=[]
        for item in items:
            total += item.get_total_price()
            desc={item.__str__():item.get_total_price()}
            description.append(desc)
        cart= Cart.objects.create(
            cart_id=user
        )
        cart.products.add(*items)
        
        
        return Response(
            {
                "price":total,
                "items":description

            }
        )

class CreatePayment(APIView):
    
    '''get cartid,get the total price,then create the invoice using cart.items as description, save the payment hash.'''
    pass

class ConfirmPayment(APIView):
    pass
        


# class CreateCart():
#     pass









