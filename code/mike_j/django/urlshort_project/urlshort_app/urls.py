from django.urls import path
from . import views

app_name = 'urlshort_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_url/', views.add_url, name='add_url'),
    path('<int:id>', views.sendview, name='send')
]