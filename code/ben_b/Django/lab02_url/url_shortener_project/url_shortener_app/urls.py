from django.urls import path
from . import views

app_name = 'url_shortener_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('mycreate/', views.mycreate, name='mycreate'),
    path('<str:url_short>/', views.new_site, name='shorter_url'),
]