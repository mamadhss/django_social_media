from django.urls import path

app_name = 'App_Posts'
from . import views

urlpatterns = [
    path('',views.home,name='home')
]