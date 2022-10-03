from django.urls import path
from . import views

app_name = 'todo_list_app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_new_objective', views.new_objective, name='add_new_objective'),
    path('edit/<int:id>/', views.edit_objective, name='edit_objective'),
    path('add_new_note', views.new_note, name='add_new_note'),
    path('delete_old_note/<int:id>/', views.delete_note, name='delete_old_note')
]