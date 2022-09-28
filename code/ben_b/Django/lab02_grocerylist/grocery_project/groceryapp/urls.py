from django.urls import path
from . import views

app_name = 'groceryapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('create_list/', views.create_list, name='create_list'),
    path('edit/<int:id>/', views.edit_list, name='edit_list')
]