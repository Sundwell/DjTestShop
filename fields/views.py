from django.views.generic import ListView
from .models import MyFields


class AllFieldsView(ListView):
    model = MyFields
    template_name = 'fields/fields_view.html'

