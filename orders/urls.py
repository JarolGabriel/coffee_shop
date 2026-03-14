from django.urls import path

from .views import MyOrderView

urlpatterns = [path("mi-order", MyOrderView.as_view(), name="my_order")]
