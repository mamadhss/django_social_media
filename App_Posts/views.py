from django.shortcuts import render,HttpResponse


def home(request):

    return render(request,'App_Posts/home.htm',context={'title':'HomePage'})
