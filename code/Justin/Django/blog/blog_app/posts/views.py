from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
# Create your views here.


# def home(request):
#     post = Post.objects.all()
#     content = {
#         'posts': post
#     }
#     return render(request, 'home.html', content)


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
