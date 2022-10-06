from django.urls import path
from . import views

app_name = 'url_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_url', views.add_url, name='add_url'),
    path('<int:id>', views.sendview, name='send'),
    # path('delete/<int:id>', views.delete_url, name='delete_url'),
]
