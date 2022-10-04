from django.urls import path
from . import views

app_name = 'urlshort_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('shorten/', views.shorten, name='shorten')
]