from django.urls import path

from . import views
from .views import ProductCreateAPI, ProductFormView, ProductListAPI, product_list

urlpatterns = [
    path("", views.product_list, name="home"),
    path("agregar/", ProductFormView.as_view(), name="add_product"),
    path("listado_productos/", product_list, name="product_list"),
    path("api/", ProductListAPI.as_view(), name="product_list_api"),
    path("api/products/create/", ProductCreateAPI.as_view(), name="product_create_api"),
]
