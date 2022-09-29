from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('add_item/', views.add_item, name='add_item'),
    path('complete/<int:id>/', views.complete, name='complete')
]
