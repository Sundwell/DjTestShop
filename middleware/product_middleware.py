from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from shop.models import Product


class CheckExpired(MiddlewareMixin):
    def process_request(self, request):
        # Product.objects.update(expired=False)
        for product in Product.objects.filter(expired=False).values():
            if timezone.localdate() >= product['date_of_expire']:
                Product.objects.filter(id=product['id']).update(expired=True)

        if Product.objects.last():
            if Product.objects.last().add_date >= Product.objects.last().date_of_expire:
                Product.objects.last().delete()
                raise ValueError(f"You can't add an expired product.")







