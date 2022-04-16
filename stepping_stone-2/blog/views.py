from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def blog_home(request):
    # return HttpResponse("<h1> Hello World </h1>")
    return render(request, "blog/blog_home.html", {"posts":Post.objects.all()})


def home(request):
    return render(request, "blog/homepage.html", context=None)