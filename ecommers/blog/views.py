from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def index(request):
    blog=Blog.objects.all()
    return render(request,'blog/index.html',{'blog':blog})

def blogpost(request,id):
    blog=Blog.objects.filter(blog_id=id)[0]
    print(blog)
    return render(request,'blog/blogpost.html',{'blog':blog})
