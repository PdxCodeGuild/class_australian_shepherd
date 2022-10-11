from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    context = {
        'message': 'Hi World!'
    }
    return render(request, 'home.html', context)



# class SignUpView(CreateView):
#   form_class = UserCreationForm
#   template_name = 'signup.html'
#   success_url: reverse_lazy('login')
