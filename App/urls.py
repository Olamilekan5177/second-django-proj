from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index, name= 'index'),
    path('Error404/', views.index, name='Error404'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('index_2', views.index_2, name='index_2'),
    path('news/', views.news, name='news'),
    path('shop/',views.shop, name='shop'),
    path('single-news/', views.single_news, name='single_news'),
    path('single-product/', views.single_product, name='single_product'),




]
