from django.db import models

class Product(models.Model):
    medicine_name = models.CharField(max_length=255)
    expiry_date = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.medicine_name

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    medicine_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    user_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    class Meta:
        db_table = 'orders'
    
    def __str__(self):
        return f"Order {self.id} - {self.medicine_name}"