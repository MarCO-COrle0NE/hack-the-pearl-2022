#from msilib.schema import ListView
from django.shortcuts import render
from django.http import HttpResponse
#from requests import post

#marco
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

def blog_home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/blog_home.html", context)
    
# Create your views here.
#def blog_home(request):
    # return HttpResponse("<h1> Hello World </h1>")
    #return render(request, "blog/base.html", context=None)


def home(request):
    return render(request, "blog/homepage.html", context=None)