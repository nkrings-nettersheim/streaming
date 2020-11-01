from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'heuser'

urlpatterns = [
    path('', views.index, name='index'),
    path('hls/', views.hls, name='hls'),
]