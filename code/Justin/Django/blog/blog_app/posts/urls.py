from django.urls import path
from posts import views

app_name = 'posts'
urlpatterns = [
    path('', views.ListPosts.as_view(), name='home'),
    path('posts/new/', views.CreatePost.as_view(), name='new'),
    path('posts/<int:pk>/', views.ListPosts.as_view(), name='home'),
]
