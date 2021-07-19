from django.conf.urls import url
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model


# Create your models here.

# CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name





# PRODUCT
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    tag = models.CharField(max_length=2,unique=True)
    availablity = models.BooleanField(default=True)
    price = models.FloatField(max_length=10)
    updated_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['category','tag','price']

    def __str__(self):
        return '{} ----- {}'.format(self.category,self.item_name)






# CART
class Cart(models.Model):
    cart = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['cart','-created_at']

    def __str__(self):
        return f'{self.cart}'

    



# class OrderItem(models.Model):
#     order = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='order_items')
#     price = models.IntegerField()
#     quantity = models.PositiveSmallIntegerField(default=1)

    # def __str__(self):
    #     return str(self.id)

#     def get_cost(self):
#         return self.price * self.quantity