# 
#  FILE		      : urls.py
#  PROJECT		  : Django-blog
#  PROGRAMMER	  : Victor Barbosa
#  FIRST VERSION  : 2022-07-01
#  DESCRIPTION	  : This file contains the URL patterns for the blog app.
# 



from django.urls import path
from . import views



# URL patterns for the blog app
urlpatterns = [
    path("", views.BlogIndexView.blog_index, name= 'blog-index'),
    path("posts/<slug>", views.BlogPostView.as_view(), name = 'blog-post'), 
    path("posts", views.BlogAllPosts.blog_all_posts, name='blog-all-posts'),
    path("read-later", views.ReadLaterView.as_view(), name="read-later" )
]
