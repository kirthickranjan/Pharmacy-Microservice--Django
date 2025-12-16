from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    medicineName = serializers.CharField(source='medicine_name')
    expiryDate = serializers.CharField(source='expiry_date')
    
    class Meta:
        model = Product
        fields = ['id', 'medicineName', 'expiryDate', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    medicineName = serializers.CharField(source='medicine_name')
    userEmail = serializers.EmailField(source='user_email', read_only=True)
    orderDate = serializers.DateTimeField(source='order_date', read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'medicineName', 'quantity', 'userEmail', 'orderDate', 'status']