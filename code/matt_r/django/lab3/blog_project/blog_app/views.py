from pdb import post_mortem
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Blog




# def myview(request):
#     context = {
#         'message': 'Hello World!'
#     }
#     return render(request, 'base.html', context)

class ListPost(ListView):
    model = Blog
    template_name = 'home.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog_app:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
