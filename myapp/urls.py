from django.urls import path
from .views import (
    category,
    category_update,
    category_delete,
    product,
    product_update,
    product_delete,
)

urlpatterns = [
    path("categories/", category, name="category"),
    path("categories/<int:pk>/update/", category_update, name="category_update"),
    path("categories/<int:pk>/delete/", category_delete, name="category_delete"),
    path("products/", product, name="product"),
    path("products/<int:pk>/update/", product_update, name="product_update"),
    path("products/<int:pk>/delete/", product_delete, name="product_delete"),
]