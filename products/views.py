from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from products.models import Product

from .forms import ProductForm


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        Product.objects.create(
            name=form.cleaned_data["name"],
            description=form.cleaned_data["description"],
            price=form.cleaned_data["price"],
            available=form.cleaned_data["available"],
            photo=form.cleaned_data["photo"],
        )

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ("POST", "PUT"):
            kwargs.update(
                {
                    "data": self.request.POST,
                    "files": self.request.FILES,  # ← ESTO ES LO IMPORTANTE
                }
            )
        return kwargs


def product_list(request):
    # 1. Obtener todos los productos
    products = Product.objects.all()

    # 2. Pasar los productos al template
    return render(request, "products/product_list.html", {"products": products})
