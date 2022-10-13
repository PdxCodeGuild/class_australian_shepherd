from django.urls import path
from . import views

app_name = 'GroceryApp'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit_list/<int:id>/', views.edit_list, name='edit_list')
]

