from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.


class ListPosts(ListView):
    model = Post
    template_name = 'home.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'newpost.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def HomeRegister(request):

    if len(request.POST['password']) < 8:
        return redirect('posts:home')

    if request.POST['password2'] == request.POST['password']:

        user_model = User(username=request.POST['name'], password=make_password(
            request.POST['password']))
        user_model.save()
    else:
        print("not match")

    return redirect('posts:home')
