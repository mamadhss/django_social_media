from django.urls import path

app_name = 'App_Posts'
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('liked/<pk>/',views.liked,name='liked'),
    path('unliked/<pk>/',views.unliked,name='unliked'),

]