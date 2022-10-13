from django.urls import path
from . import views

app_name = 'BlogApp'
urlpatterns = [
    path('', views.profile, name='home'),
    path('/new/post/',views.create, name='new'),
    path('posts/<int:pk>/', views.profile.as_view(), name='home'),
    path('/post/<int:pk>/edit',views.EditPost, name='edit'),
    path('post/<int:pk>/delete/',views.DeletePost, name='delete')
]