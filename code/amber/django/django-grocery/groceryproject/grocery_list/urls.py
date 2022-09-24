from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.myview, name='myview'),
]
