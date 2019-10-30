from shop.models import Product


def product_count(request):
    count = Product.objects.all().count()
    print(count)
    return {'product_count': count}
