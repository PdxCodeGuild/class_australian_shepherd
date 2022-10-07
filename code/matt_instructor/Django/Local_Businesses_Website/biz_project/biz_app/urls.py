from django.urls import path
from . import views

app_name = 'biz_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('addyourwebsite', views.addsite, name="addsite"),
    path('<str:name>', views.redirect_view, name='send_to_page'),

]