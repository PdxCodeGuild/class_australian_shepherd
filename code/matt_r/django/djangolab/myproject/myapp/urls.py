from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('myview/', views.myview, name='myview')
]