from django.urls import path
from . import views

app_name = 'short_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('<id>', views.redirect_view, name='send_url'),
]
