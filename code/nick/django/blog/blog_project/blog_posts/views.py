from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from django.http import HttpResponse
from django.template import loader

# Create your views here.

class ListPosts(ListView):
    model = Post
    template_name = './blog_posts/base.html'

    def testing(request):
        template = loader.get_template('./blog_posts/posts.html')
        return HttpResponse(template.render())

class CreatePosts(LoginRequiredMixin, CreateView):
    model = Post
    template_name = './blog_users/users_write.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)