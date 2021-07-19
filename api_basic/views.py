from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Cart
from .serializers import ProductSerializer, CategorySerializer, CartSerializer
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
import stripe
from django.conf import settings
from rest_framework.views import APIView


# 1.Register APIView
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        # Check If our serializer is valid or not?
        serializer.is_valid(raise_exception=True)
        # If our serializer is valid then we are going to save serializer
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# 2.Login and Logout APIView
from rest_framework import permissions
from django.contrib.auth import  login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        serializer = AuthTokenSerializer(data=request.data)
        # Check If our serializer is valid or not?
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # create session based authentication with token based authentication
        login(request,user)
        return super(LoginAPI,self).post(request,format=None)


# 3.Category Details  
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):                      
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 4.Category List (GET request) and Filter  
class ListCategory(ListAPIView):               
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 5.Product Details
class DetailProduct(generics.RetrieveUpdateDestroyAPIView):                       
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 


# 6.Product List (GET request) and Filter
class ListProduct(ListAPIView):                        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Filteration
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('category','item_name','tag','price')


class CartList(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer 
    

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer 