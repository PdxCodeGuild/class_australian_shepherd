from django.urls import path
from . import views

app_name = 'shortapp'

urlpatterns = [
    path('', views.shortapp, name='index'),
    path('codeURL/', views.codeURL, name='codeURL'),
    path('<str:id>', views.RedirURL, name='send_to')
]
