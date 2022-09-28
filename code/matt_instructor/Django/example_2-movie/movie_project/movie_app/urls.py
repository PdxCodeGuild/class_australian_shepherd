from django.urls import path
from . import views

app_name = 'movie_app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_new_movie', views.new_movie, name='add_new_movie'),
    path('edit/<int:id>/', views.edit_movie, name='edit_movie')
]