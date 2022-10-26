from django.urls import path
from . import views

app_name = 'users_app'
urlpatterns = [
    path('signup/', views.user_register.as_view(), name='signup'),
    path('<str:username>/', views.user_profile.as_view(), name='profile')
]