from django.urls import path
from . import views

app_name = 'url_shrinker'
urlpatterns = [
    path('', views.home, name='home'),
    path('shrunk', views.submitter, name='submitter'),
    path('<short_url>', views.redirect_view, name='redirect_view')
]