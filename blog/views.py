# 
#  FILE		      : views.py
#  PROJECT		  : Django-blog
#  PROGRAMMER	  : Victor Barbosa
#  FIRST VERSION  : 2022-07-01
#  DESCRIPTION	  : This file contains the views for the blog app.
# 



from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from datetime import date
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .models import Commentary, Post
from .forms import CommentForm
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

 
 
# Home page view. It will show the last 3 posts.
class StartPageView(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ["-date"]

    # return only the last 3 posts
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data



# Renders the home page with the last 3 posts.
class BlogIndexView(View):
    def blog_index(request):
        latest_posts = Post.objects.all().order_by("-date")[:3] # The minus signal makes it descending order. It wouldn't be possible to use minus on the [:3] 
        return render(request, "blog/home.html", {
            'posts': latest_posts,
        })



# Show all the posts.
class BlogAllPosts(View):
    def blog_all_posts(request):
        all_posts = Post.objects.all().order_by("-date")
        return render(request, "blog/all_posts.html", {
            'all_posts': all_posts,
        })



# Show a single post.
class BlogPostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later =  post_id in stored_posts
        else:
            is_saved_for_later = False 
        return is_saved_for_later

    def get(self, request, slug):
        identified_post = Post.objects.get(slug = slug) #if you want the 404 error: "get_object_or_404(Post,slug=slug)" need to import it       
        all_comments = Commentary.objects.filter(post = identified_post).order_by("-date")   
        context = {
            'post': identified_post,
            'tags': identified_post.tag.all(),
            "comment" : CommentForm(),
            "all_comments": all_comments,
            "is_saved_for_later": self.is_stored_post(request, identified_post.id),
        }        
        return render (request, 'blog/blog_post.html',context)
    
    def post(self, request, slug):
        form = CommentForm(request.POST)
        identified_post = Post.objects.get(slug = slug)
                
        if form.is_valid():
            form.save().post = Post.objects.get(slug = slug)
            form.save()
            return HttpResponseRedirect(reverse("blog-post", args = [slug]))
        
        else:
            context = {
            "post": identified_post,
            "tags": identified_post.tag.all(),
            "comment": form,
            "all_comments": identified_post.comments.all().order_by("-id"), 
            #"all_comments": Commentary.objects.filter(post = identified_post).order_by("-date")
            "is_saved_for_later": self.is_stored_post(request, identified_post.id)
            }
        return render(request, "blog/blog_post.html", context)
        


# Read later.
class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts) #this will get all the posts whose 'id' are in the 'stored_posts' list. you need to use double underscore: 'id__in'.
            context["posts"] = posts.order_by("title")
            context["has_posts"] = True

        return render(request, "blog/stored_posts.html", context)
    
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        post_id = int(request.POST["post_id"])

        if stored_posts is None:
            stored_posts = []
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts

        return redirect(request.META['HTTP_REFERER'])
    
    
    
# Define 404 error
def handler404(request, exception):
    return render(request, '404.html', {})



# -- API VIEWS --

# All posts
class PostListAPIView(APIView):
    """
    List all posts
    
    Args:
        request: The HTTP request object.
        pk: The primary key of the post to retrieve.
    
    Returns:
        If the post exists, returns serialized data with a 200 OK response.
        If the post does not exist, returns a 404 Not Found response.
    """
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    """
    Create a new post
    
    Args:
        request: The HTTP request object.
        pk: The primary key of the post to retrieve.
        
    Returns:
        If the serializer is valid, returns serialized data with a 201 Created response.
        If the serializer is invalid, returns a 400 Bad Request response with validation errors. 
    """ 
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Single post
class PostDetailAPIView(APIView):
    def get(self, request, pk):
        """
        Retrieve a specific post by its primary key (pk).

        Args:
            request: The HTTP request object.
            pk: The primary key of the post to retrieve.

        Returns:
            If the post exists, returns serialized data with a 200 OK response.
            If the post does not exist, returns a 404 Not Found response.
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk):
        """
        Update an existing post by its primary key (pk).

        Args:
            request: The HTTP request object containing updated data.
            pk: The primary key of the post to update.

        Returns:
            If the post exists and the serializer is valid, returns serialized data with a 200 OK response.
            If the serializer is invalid, returns a 400 Bad Request response with validation errors.
            If the post does not exist, returns a 404 Not Found response.
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    

        
    def delete(self, request, pk):
        """
        Delete a specific post by its primary key (pk).

        Args:
            request: The HTTP request object.
            pk: The primary key of the post to delete.

        Returns:
            If the post exists, returns a 204 No Content response.
            If the post does not exist, returns a 404 Not Found response.
        """
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)