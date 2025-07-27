from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='Shop/media/uploads')
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.title
    


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart of {self.user.username}' 
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
    


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f'{self.product.title}'


from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    