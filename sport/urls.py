from django.urls import path

from sport.views import ShowSpFieldsView, DeleteField, DeleteFieldView
from .views import ShowSportsmenView, AddSportsmanView, ShowProfileView, ShowFieldView

app_name = 'sport'

urlpatterns = [
    path('sp_list/', ShowSportsmenView.as_view(), name='sp_list'),
    path('sp_list/profile/<int:pk>/', ShowProfileView.as_view(), name='sp_profile'),
    path('sp_list/add/', AddSportsmanView.as_view(), name='sp_add'),
    path('sp_list/profile/<int:pk>/fields/', ShowSpFieldsView.as_view(), name='sp_fields_list'),
    path('field/<int:pk>/', ShowFieldView.as_view(), name='sp_field'),
    path('field/delete/<int:pk>/', DeleteFieldView.as_view(), name='sp_field_delete'),
    path('ajax/field/delete/',  DeleteField.as_view(), name='field_ajax_delete'),
]