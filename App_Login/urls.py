from django.urls import path,include
from . import views
app_name = 'App_Login'

urlpatterns = [
   path('signup/',views.sign_up,name='sign_up'),
   path('login/',views.login_page,name='login'),
   path('edit/',views.edit_profile,name='edit'),
   path('logout/',views.logout_user,name='logout'),
   path('profile/',views.profile,name='profile'),
   path('user/<slug:slug>/',views.user,name='user'),
   path('follow/<slug:slug>/',views.follow,name='follow'),
   path('unfollow/<slug:slug>/',views.unfollow,name='unfollow'),
   
]   