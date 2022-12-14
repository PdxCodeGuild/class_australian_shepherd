from django.urls import path
from . import views

app_name = 'shortener_app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create, name='create'),
    path('<int:id>', views.redirect_view, name= 'redirect_view')
]