from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
# def home(request):
#     all_gravy = Post.objects.all()
#     context = {
#         'all_gravy' :                           
#     }
#     return render(request, '')

################ WE USE CLASS BASED VIEWS ONLY NOW ################

class ListPosts(ListView):
    model: Post
    template_name: 'home.html'

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title','body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    template_name = 'edit_post.html'
    fields = ['title', 'body']
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('gravy_app:home')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author