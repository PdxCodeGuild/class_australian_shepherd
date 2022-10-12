from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Post

class CreatePost(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

class ListPost(ListView):
    model = Post
    template_name = 'home.html'