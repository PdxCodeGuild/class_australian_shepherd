from django.urls import path
from . import views

app_name = 'blog_posts'
urlpatterns = [
    path('', views.ListPosts.as_view(), name='home'),
]