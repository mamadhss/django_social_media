from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from App_Login.models import Follow
from .models import Post,Like
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)


    
    search = request.GET.get('search')
    users = User.objects.all()
    if search:
        users = users.filter(username__icontains=search)
       

    context = {
        'title':'home page',
        'search':search,
        'users':users,
        'posts':posts,
        'liked_post':liked_post,
        'liked_post_list': liked_post_list
    }
      

    return render(request,'App_Posts/home.htm',context)

@login_required(login_url=settings.LOGIN_URL)
def liked(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post = Like(post=post,user=request.user)
        liked_post.save()
        return HttpResponseRedirect(reverse('App_Posts:home'))

@login_required(login_url=settings.LOGIN_URL)
def unliked(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Posts:home'))
