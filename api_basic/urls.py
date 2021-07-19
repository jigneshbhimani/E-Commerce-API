from django.urls import path,include

from knox import views as knox_views

from .views import (
        CartList,
        DetailCart,
        LoginAPI,
        RegisterAPI,
        DetailCategory,
        DetailProduct,
        ListProduct,
        ListCategory,
)

from . import views

urlpatterns = [

    path('register/',RegisterAPI.as_view(),name='register'),                 
    path('login/',LoginAPI.as_view(),name='login'),    
    path('logout/',knox_views.LogoutView.as_view(),name='logout'),

    path('productlist/',ListProduct.as_view(),name='products'),
    path('products/<int:pk>',DetailProduct.as_view()),

    path('categorylist/',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>',DetailCategory.as_view()),

    path('carts/',CartList.as_view(),name='cartlist'),
    path('carts/<int:pk>',DetailCart.as_view()),

]
