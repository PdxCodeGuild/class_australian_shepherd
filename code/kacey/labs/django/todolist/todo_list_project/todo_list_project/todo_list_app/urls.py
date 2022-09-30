from django.urls import path
from . import views

app_name = 'todo_list_app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_new_objective', views.new_objective, name='add_new_objective'),
    path('edit/<int:id>/', views.edit_objective, name='edit_objective')
]