from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404



# Create your views here.

# def home(request):
#     context = {
#         'message': 'Hi World!'
#     }
#     return render(request, 'home.html', context)


class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = 'signup.html'
  success_url: reverse_lazy('login')

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
