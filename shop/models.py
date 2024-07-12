
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# 蛋糕
class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='cakes/')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True) #確認新增的字段

    def __str__(self):
        return f'{self.user.username} - {self.cake.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    
# 產品
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
# from django.contrib.auth.models import User
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem') #S

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #n S
    quantity = models.PositiveBigIntegerField(default=0)

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='OrderItem')
#     total_price = models.DecimalField(max_digits=10,decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE) #n S
#     quantity = models.PositiveIntegerField()