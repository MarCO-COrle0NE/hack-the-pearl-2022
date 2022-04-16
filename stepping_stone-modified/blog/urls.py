from django.urls import path, include


#marco
from .views import PostListView, PostDetailView, PostCreateView
from . import views
urlpatterns=[
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('', views.home, name='homepage'),
    
]

#urlpatterns=[
#    path('blog/', views.blog_home, name='blog-home'),
#    path('', views.home, name='homepage'),
    
#]