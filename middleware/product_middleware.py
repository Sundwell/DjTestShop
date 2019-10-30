from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from shop.models import Product


class ProductError(Exception):
    pass


class CheckExpired(MiddlewareMixin):

    def process_request(self, request):
        # Product.objects.update(expired=False)
        for product in Product.objects.filter(expired=False).values():
            if timezone.localdate() >= product['date_of_expire']:
                Product.objects.filter(id=product['id']).update(expired=True)

        pr_last = Product.objects.last()
        if pr_last:
            if pr_last.add_date >= pr_last.date_of_expire:
                pr_last.delete()
                raise ProductError(f"You can't add an expired product.")









