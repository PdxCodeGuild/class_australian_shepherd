from django.urls import path
from . import views

app_name = 'BlogApp'
urlpatterns = [
    path('', views.profile.as_view(), name='home'),
    path('new/post/',views.create.as_view(), name='new'),
    path('posts/<int:pk>/', views.profile.as_view(), name='home'),
    path('post/<int:pk>/edit',views.EditPost.as_view(), name='edit'),
    path('post/<int:pk>/delete/',views.DeletePost.as_view(), name='delete')
]
