from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

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

    def dispatch(self, request, *args, **kwargs):
        self.sportsman = get_object_or_404(Sportsman, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowSpFieldsView, self).get_context_data(**kwargs)
        context['sp_id'] = self.kwargs['pk']
        context['myfields_list'] = MyFields.objects.filter(sportsman_id=self.kwargs['pk'])
        return context


class ShowFieldView(DeleteView):
    model = MyFields
    template_name = 'fields/fields_view.html'
    success_url = reverse_lazy('sport:sp_list')

