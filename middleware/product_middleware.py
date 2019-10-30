from shop.models import Product


class AlwaysFreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        Product.objects.update(expired=False)

        return response
