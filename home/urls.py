from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = 'index'),
    path('about/',views.about,name = 'about'),
    path('product/<int:id>',views.product,name = 'products'),
    path('product/',views.product,name = 'product'),
    path('productsingle/<int:id>',views.productsingle,name = 'productsingle'),
    path('productsingle/',views.productsingle,name = 'productsingles'),
    path('cart/',views.cart,name = 'cart'),

    path('cart_add/<int:pk>',views.cart_add,name='cart_add'),
    path('cart_remove/<int:pk>',views.cart_remove,name='cart_remove'),


    path('checkout/',views.checkout,name = 'checkout'),

]