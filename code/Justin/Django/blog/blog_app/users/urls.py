from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('users/home/', views.HomeView.as_view(), name='home'),
    path('users/signup/', views.Register.as_view(), name='signup'),
    path('<str:username>', views.Profile.as_view(), name='profile'),
]
