from django.contrib import admin
from .models import Payment, Cart, Category, Product, CartItem


# Register your models here.
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(CartItem)
