from django.views.generic import ListView, DeleteView, FormView
from django.urls import reverse_lazy
from shop.models import Product

from .forms import ProductAddForm


class ProductPageView(ListView):
    model = Product
    template_name = 'shop/pr_list.html'


class AddProductView(FormView):
    model = Product
    form_class = ProductAddForm
    template_name = 'shop/pr_add.html'
    success_url = reverse_lazy('shop:products')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class ShowDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product.html'
    success_url = reverse_lazy('shop:products')
