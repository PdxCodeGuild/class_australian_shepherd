from unicodedata import name
from django.urls import path
from . import views
app_name = 'urlshortner_app'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('new_url', views.new_url, name="new_url" ),
    path('<int:id>', views.redirect_view, name="redirected_view")
]
