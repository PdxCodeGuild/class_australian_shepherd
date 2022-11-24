from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
# from django.contrib.auth.models import User
from users.models import CustomUser
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUserChangeForm
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
        