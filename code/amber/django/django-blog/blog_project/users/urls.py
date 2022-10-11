from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('<str:username>/', views.ProfileView.as_view(), name='profile')
]
