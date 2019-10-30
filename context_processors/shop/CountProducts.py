from shop.models import Product


def product_count(request):
    return {'product_count': Product.objects.all().count()}
