from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

def home(request):
    
    search = request.GET.get('search')
    users = User.objects.all()
    if search:
        users = users.filter(username__icontains=search)
       

    context = {
        'title':'home page',
        'search':search,
        'users':users,
    }
      

    return render(request,'App_Posts/home.htm',context)
