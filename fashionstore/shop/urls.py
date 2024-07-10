from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('categories/', views.categories, name='categories'),  # Add this line
    path('categories/men/', views.category_men, name='category_men'),
    path('categories/women/', views.category_women, name='category_women'),
    path('categories/kids/', views.category_kids, name='category_kids'),
    path('product/<int:product_id>/', views.product_details, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
