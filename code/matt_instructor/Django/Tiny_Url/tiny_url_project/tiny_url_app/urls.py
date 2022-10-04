from django.urls import path
from . import views

app_name = 'tiny_url_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('tiny_url_app/<str:short_url>/', views.redirect, name='redirect'),
]