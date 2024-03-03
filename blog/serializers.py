# 
#  FILE		      : serializers.py
#  PROJECT		  : Django-blog
#  PROGRAMMER	  : Victor Barbosa
#  FIRST VERSION  : 2022-07-01
#  DESCRIPTION	  : This file contains the serializers for the blog app.
# 



from rest_framework import serializers
from blog.models import Post



# Post serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'date', 'image', 'excerpt', 'tag', 'content', 'slug']
