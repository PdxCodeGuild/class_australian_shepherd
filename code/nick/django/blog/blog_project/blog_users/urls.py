from django.urls import path
from . import views

app_name = 'blog_users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile')
]
    # path('registered', views.successful, name='registersuccess'),