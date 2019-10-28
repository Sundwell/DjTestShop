from django.views import View
from django.views.generic import ListView, DeleteView, FormView, DetailView, TemplateView
from django.urls import reverse_lazy
from shop.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductAddForm


class ProductPageView(ListView):
    model = Product
    template_name = 'shop/pr_list.html'


class AddProductView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('user:login')
    model = Product
    form_class = ProductAddForm
    template_name = 'shop/pr_add.html'
    success_url = reverse_lazy('shop:products')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class ShowDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('user:login')
    model = Product
    template_name = 'shop/product.html'
    success_url = reverse_lazy('shop:products')


class MainPageView(TemplateView):
    template_name = 'base.html'
