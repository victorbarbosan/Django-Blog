from django.urls import path
from . import views





urlpatterns = [
    path("", views.BlogIndexView.blog_index, name= 'blog-index'),
    path("posts/<slug>", views.BlogPostView.as_view(), name = 'blog-post'), #/posts/my-first-post
    path("posts", views.BlogAllPosts.blog_all_posts, name='blog-all-posts'),
    path("read-later", views.ReadLaterView.as_view(), name="read-later" )
]
