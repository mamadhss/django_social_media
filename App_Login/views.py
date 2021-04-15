from django.shortcuts import render,HttpResponseRedirect
from .forms import CreateNewUser,EditProfile
from .models import UserProfile,Follow
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from App_Posts.forms import PostForm
from django.contrib.auth.models import User


def sign_up(request):
    form =  CreateNewUser()
    registered = False

    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created successfully')
            registered = True
            return HttpResponseRedirect(reverse('App_Login:login'))

    context = {
        'form':form,
        'registered':registered,
        'title':'Signup From Here'
    }        

    return render(request,'App_Login/signup.htm',context)        


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Login:edit'))
    context = {
        'title':'Login Page',
        'form':form

    }            

    return render(request,'App_Login/login.htm',context)  

@login_required(login_url=settings.LOGIN_URL)
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated!')
            return HttpResponseRedirect(reverse('App_Login:profile'))
            #form.save(commit=True)
            
    context = {
        'title':'Edit Profile Page',
        'form':form,
    }
    return render(request,'App_Login/profile.htm',context)

@login_required(login_url=settings.LOGIN_URL)    
def logout_user(request):
    logout(request)
    messages.success(request,'successfully logged out')
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required(login_url=settings.LOGIN_URL) 
def profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()    
            return HttpResponseRedirect(reverse('App_Posts:home'))   

    context = {
        'form':form
    }             

    return render(request,'App_Login/user.htm',context)


        
@login_required(login_url=settings.LOGIN_URL) 
def user(request,slug):
    user_other = User.objects.get(username=slug)
   
    already_followed = Follow.objects.filter(follower=request.user,following=user_other)

    if user_other == request.user:

        return HttpResponseRedirect(reverse('App_Login:profile'))

        
    
    context = {
        'user_other':user_other,
        'already_followed':already_followed 

    }
    return render(request,'App_Login/user_other.htm',context)

@login_required(login_url=settings.LOGIN_URL) 
def follow(request,slug):
    following_user = User.objects.get(username=slug)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user,following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user,following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_Login:user', kwargs={'slug':slug}))

@login_required(login_url=settings.LOGIN_URL) 
def unfollow(request,slug):
    following_user = User.objects.get(username=slug)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user,following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_Login:user',kwargs={'slug':slug}))


        

        
