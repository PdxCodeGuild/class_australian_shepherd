from re import template
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from .models import blog_post
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Home(ListView):
    model = blog_post
    template_name = 'home.html'

class create(CreateView, LoginRequiredMixin):
    model = blog_post
    template_name = 'new_post.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = blog_post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = blog_post
    template_name = 'del_post.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
