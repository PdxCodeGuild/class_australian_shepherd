from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.ListPost.as_view(), name='home'),
    path('post/new/', views.CreatePost.as_view(), name='new'),
    path('posts/<int:pk>/', views.ListPost.as_view(), name='home'),
    path('posts/<int:pk>/edit', views.EditPost.as_view(), name='edit'),
    path('posts/<int:pk>/delete/', views.DeletePost.as_view(), name='delete')
]