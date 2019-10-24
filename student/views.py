from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import \
    RedirectView, TemplateView, View, \
    DetailView, CreateView, DeleteView, FormView, UpdateView, \
    ListView
from .models import Student
from .forms import StudentUpdateForm, StudentAddForm


class MainPageView(TemplateView):
    template_name = 'base.html'


class StudentsListView(ListView):
    model = Student
    template_name = 'student/students.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_about.html'


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_delete.html'
    success_url = reverse_lazy('student:students')


# class StudentAddView(CreateView):
#     model = Student
#     template_name = 'student/student_add.html'
#     fields = [
#         'first_name',
#         'last_name',
#         'year',
#     ]
#     success_url = reverse_lazy('student:students')


class StudentAddView(FormView):
    model = Student
    form_class = StudentAddForm
    template_name = 'student/student_add.html'
    success_url = reverse_lazy('student:students')
    
    def form_valid(self, form):
        form.save()
        return super(StudentAddView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'student/student_update.html'

    def get_success_url(self):
        return reverse_lazy('student:student', args=[self.kwargs['pk']])
