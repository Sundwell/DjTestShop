from django.contrib import admin
from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_name', 'product_photo']}),
        ('Dates', {'fields': ['add_date', 'date_of_expire']}),
        ('Description', {'fields': ['description']})
    ]


admin.site.register(Product, ProductAdmin)
