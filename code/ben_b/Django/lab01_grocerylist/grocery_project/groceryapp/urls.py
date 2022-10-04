from django.urls import path
from . import views

app_name = 'groceryapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('create_list/', views.create_list, name='create_list'),
    path('edit_bool/<int:id>/', views.edit_bool, name='edit_bool'),
    path('edit_grocery_item/<int:id>/', views.edit_grocery_item, name='edit_grocery_item'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post')
]