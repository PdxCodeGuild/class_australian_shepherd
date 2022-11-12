from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.myview, name='home'),
    path('MyItems/', views.MyItems, name='MyItems'),
    path('Completed/<int:pk>/', views.Completed, name='Completed'),
    path('Delete_Item/<int:id>', views.Delete_Item, name='Delete_Item'),
]
