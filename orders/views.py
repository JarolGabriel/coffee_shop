from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.serializers import OrderSerializer

from .form import OrderProductForm
from .models import Order, OrderProduct


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"
    login_url = "/usuarios/login/"

    def get_object(self, queryset=None):
        return Order.objects.filter(user=self.request.user, is_active=True).first()


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")
    login_url = "/usuarios/login/"

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()

        product_name = form.instance.product.name
        messages.success(
            self.request, f'¡Producto "{product_name}" agregado al pedido!'
        )

        return super().form_valid(form)


class UpdateOrderProductView(LoginRequiredMixin, View):
    """Vista para aumentar o disminuir la cantidad de un producto"""

    login_url = "/usuarios/login/"

    def post(self, request, pk):
        product_order = get_object_or_404(
            OrderProduct, pk=pk, order__user=request.user, order__is_active=True
        )

        action = request.POST.get("action")

        if action == "increase":
            product_order.quantity += 1
            product_order.save()
        elif action == "decrease" and product_order.quantity > 1:
            product_order.quantity -= 1
            product_order.save()

        return redirect("my_order")


class DeleteOrderProductView(LoginRequiredMixin, View):
    """Vista para eliminar un producto del pedido"""

    login_url = "/usuarios/login/"

    def post(self, request, pk):
        product_order = get_object_or_404(
            OrderProduct, pk=pk, order__user=request.user, order__is_active=True
        )
        product_order.delete()

        return redirect("my_order")


class OrderCreateAPI(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

    def post(self, request):
        # Pasar el request al serializer (para que tenga acceso a request.user)
        serializer = OrderSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_4000_BAD_REQUEST)
