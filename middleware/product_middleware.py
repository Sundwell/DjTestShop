from django.utils.deprecation import MiddlewareMixin
from shop.models import Product


class AlwaysFreshMiddleware(MiddlewareMixin):

    def __call__(self, request):

        response = self.get_response(request)
        Product.objects.update(expired=False)

        return response
