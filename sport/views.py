from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, View

from fields.models import MyFields
from .models import Sportsman
from .forms import SportsmanForm


class ShowSportsmenView(ListView):
    model = Sportsman
    template_name = 'sport/sportsmen_list.html'


class ShowProfileView(DetailView):
    model = Sportsman
    template_name = 'sport/profile.html'


class AddSportsmanView(CreateView):
    form_class = SportsmanForm
    template_name = 'sport/add_sportsman.html'


class ShowSpFieldsView(ListView):
    model = MyFields
    template_name = 'sport/sp_fields.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowSpFieldsView, self).get_context_data(**kwargs)
        context.update({'sp_id': self.kwargs['pk']})
        context.update({'myfields_list': MyFields.objects.filter(sportsman_id=self.kwargs['pk'])})
        return context


class ShowFieldView(DetailView):
    model = MyFields
    template_name = 'fields/fields_view.html'


class DeleteFieldView(DeleteView):
    model = MyFields
    template_name = 'sport/delete_field.html'
    success_url = reverse_lazy('sport:sp_list')


class DeleteField(View):

    def get(self, request):
        print(request.GET)
        id1 = request.GET.get('id', None)
        MyFields.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
