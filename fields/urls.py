from django.urls import path
from .views import AllFieldsView

app_name = 'fields'

urlpatterns = [
    path('fields/', AllFieldsView.as_view(), name='fields')
]