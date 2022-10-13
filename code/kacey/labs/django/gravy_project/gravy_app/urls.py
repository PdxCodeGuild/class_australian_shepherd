from django.urls import path
from . import views

app_name = 'gravy_app'
urlpatterns = [
    path('', views.ListPosts.as_view(), name='home'),
    path('gravy_app/new_post/', views.CreatePost.as_view(), name='new_post'),
    path('gravy_app/<int:pk>/', views.ListPosts.as_view(), name='home'),
    path('gravy_app/<int:pk>/edit_post', views.EditPost.as_view(), name='edit_post'),
    path('gravy_app/<int:pk>/delete_post/', views.DeletePost.as_view(), name='delete_post')
]
