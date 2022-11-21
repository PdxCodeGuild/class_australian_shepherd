# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
# from django.contrib.auth.models import User
from users.models import CustomUser
from django.contrib.auth.hashers import make_password

# def home(request):
#     all_posts = Post.objects.all()
#     context = {
#         'posts' : all_posts
#     }
#     return render(request, 'home.html', context)

class ListPosts(ListView):
    model = Post
    template_name = 'home.html'

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def HomeRegister(request):

    # example of password requirements
    if len(request.POST['password']) < 8:
        return redirect('posts:home')

    if request.POST['password2'] == request.POST['password']:
        # print('password', request.POST['password'])
        # print('hashed password', make_password(request.POST['password']))

        user_model = CustomUser(username=request.POST['name'], password=make_password(request.POST['password']))
        user_model.save()
    else:
        print("not match")

    return redirect('posts:home')