from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.myview, name='home'),
    path('mycreate/', views.mycreate, name='mycreate')
]
