from django.urls import path
from . import views


app_name = 'grocerylist'
urlpatterns = [
    path('', views.home, name='home'),
    path('addtolist/', views.listcreation, name='listcreation'),
    path('myview/', views.myview, name='myview'),
    path('edit/<int:id>/', views.edit_task, name='edittask'),
    path('delete/<int:id>/',views.delete_task, name='deletetask')
]