from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from App_Login.models import Follow
from .models import Post
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))


    
    search = request.GET.get('search')
    users = User.objects.all()
    if search:
        users = users.filter(username__icontains=search)
       

    context = {
        'title':'home page',
        'search':search,
        'users':users,
        'posts':posts
    }
      

    return render(request,'App_Posts/home.htm',context)
