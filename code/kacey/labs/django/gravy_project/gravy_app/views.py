from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import BlogPost

# Create your views here.
# def home(request):
#     all_gravy = Post.objects.all()
#     context = {
#         'all_gravy' :                           
#     }
#     return render(request, '')

################ WE USE CLASS BASED VIEWS ONLY NOW ################

class ListPosts(ListView):
    model = BlogPost
    template_name = 'home.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'new_post.html'
    fields = ['title','body']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost 
    template_name = 'edit_post.html'
    fields = ['title', 'body', 'is_public']
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
    
class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('gravy_app:home')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user