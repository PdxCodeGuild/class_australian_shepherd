from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import blog_post

# from django.Blog.myproject.my_blog.BlogApp.models import blog_post

# def home(request):
#     posts = blog-post
#     context = {
#         'posts' : posts
#     }
#     return render(request, 'BlogApp/home.html', context)

class profile(ListView):
    model = blog_post
    template_name = 'home.html'

class create(CreateView, LoginRequiredMixin):
    model = blog_post
    template_name = 'new_post.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = blog_post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = blog_post
    template_name = 'del_post.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author