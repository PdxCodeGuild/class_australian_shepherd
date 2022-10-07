from django.urls import path
from .import views

appname = "myname"
urlpatterns = [
    path('myview/', views.myview, name='myview')
]

from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('myview/', views.myview, name='myview'),
    path('mycreate/', views.mycreate, name='mycreate')
]