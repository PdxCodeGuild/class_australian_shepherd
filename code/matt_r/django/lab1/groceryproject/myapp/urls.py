from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.homeview, name='home'),
    path('add_new_item', views.new_item, name='add_new_item'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item')

]