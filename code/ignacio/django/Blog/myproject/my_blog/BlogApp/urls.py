from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/',views.create.as_view(), name='create'),
    path('edit/<int:pk>/',views.EditPost.as_view(), name='edit'),
    path('delete/<int:pk>/',views.DeletePost.as_view(), name='delete')
]
