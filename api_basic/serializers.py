from django.db import models
from rest_framework import serializers 
from django.contrib.auth.models import User
from api_basic.models import Category, Product, Cart
from rest_framework.fields import Field

# 1.User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']


# 2.Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self,validated_date):
        user  = User.objects.create_user(validated_date['username'],validated_date['email'],validated_date['password'])
        return user


# 3.Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','date_created']


# 4.Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category','item_name','tag','price','description','date_created','availablity','updated_at']


# 5.Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    cart = UserSerializer(many=False)
    products = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['cart','created_at','products','quantity']

