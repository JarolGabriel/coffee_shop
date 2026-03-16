from rest_framework.serializers import ModelSerializer

from .models import Order, OrderProduct


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["product", "quantity"]


class OrderSerializer(ModelSerializer):
    products = OrderProductSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "is_active", "order_date", "products"]
        read_only_fields = ["id", "user", "order_date"]

    def create(self, validated_data):

        products_data = validated_data.pop("products")

        user = self.context["request"].user

        order = Order.objects.create(user=user)

        for product_data in products_data:
            OrderProduct.objects.create(
                order=order,
                product=product_data["product"],
                quantity=product_data["quantity"],
            )

        return order
