from django.db import models
from user.models import User


class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product_name = models.CharField('Product name', max_length=50)
    add_date = models.DateField('Add date')
    date_of_expire = models.DateField('Date of expire')
    product_photo = models.ImageField('Product photo', upload_to='shop/images')
    expired = models.BooleanField(default=False)
    description = models.TextField('About Product', blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.add_date and self.date_of_expire:
            self.expired = self.add_date >= self.date_of_expire
        if not self.description:
            self.description = 'No description'
        super(Product, self).save()

    def __str__(self):
        return self.product_name



