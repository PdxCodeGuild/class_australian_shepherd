from django.urls import path
from . import views

app_name = 'ShortenerApp'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('transport/', views.transport, name='transport')
]