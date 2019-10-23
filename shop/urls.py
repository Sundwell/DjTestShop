from django.urls import path

from shop.views import ProductPageView, AddProductView, ShowDeleteView

app_name = 'shop'

urlpatterns = [
    path('shop/', ProductPageView.as_view(), name='products'),
    path('shop/pr_add/', AddProductView.as_view(), name='add_product'),
    path('shop/product/<int:pk>', ShowDeleteView.as_view(), name='product')
]