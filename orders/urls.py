urlpatterns = []
from django.urls import path

from .views import (
    CreateOrderProductView,
    DeleteOrderProductView,
    MyOrderView,
    UpdateOrderProductView,
)

urlpatterns = [
    path("mi-order", MyOrderView.as_view(), name="my_order"),
    path("agregar-product", CreateOrderProductView.as_view(), name="add_product"),
    path(
        "actualizar/<int:pk>/",
        UpdateOrderProductView.as_view(),
        name="update_order_product",
    ),
    path(
        "eliminar/<int:pk>/",
        DeleteOrderProductView.as_view(),
        name="delete_order_product",
    ),
]
