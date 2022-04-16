from django.urls import path, include
from . import views

urlpatterns=[
    path('blog/', views.blog_home, name='blog_home'),
    path('', views.home, name='homepage'),
    
]