from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.ListPost.as_view(), name='home'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('posts/<int:pk>/', views.ListPost.as_view(), name='home'),
]