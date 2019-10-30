from django.utils.deprecation import MiddlewareMixin
from shop.models import Product


class AlwaysFreshMiddleware(MiddlewareMixin):

    def __call__(self, request):
        Product.objects.update(expired=False)

        return super(AlwaysFreshMiddleware, self).__call__()
