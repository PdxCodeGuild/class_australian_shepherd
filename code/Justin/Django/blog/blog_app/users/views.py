from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'home'


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url: reverse_lazy('login')


class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
