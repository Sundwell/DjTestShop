from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from user.models import User
from user.forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth.hashers import make_password


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'


class UserRegistrationView(FormView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
