from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('mycreate/', views.mycreate, name='mycreate'),
    path('detail/<int:pk>/', views.detail, name="detail")
]
