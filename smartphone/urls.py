from django.urls import path
from .views import index_page, get_madel, get_product

urlpatterns = [
    path('', index_page, name="brand_list"),
    path('madel/<int:madel_id>', get_madel, name="madel_list"),
    path('product/<int:product_id>/<int:soni>', get_product, name='product_list'),
]