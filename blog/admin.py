# 
#  FILE		      : admin.py
#  PROJECT		  : Django-blog
#  PROGRAMMER	  : Victor Barbosa
#  FIRST VERSION  : 2022-07-01
#  DESCRIPTION	  : This file contains the admin settings for the blog app.
# 



from django.contrib import admin
from .models import Commentary, Post, Author, Tag


# Post settings on admin page
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("author", "date")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

admin.site.register(Author)
admin.site.register(Tag)



# Commentary settings on admin page
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "date")
    list_filter = ("author", "date")

admin.site.register(Commentary, CommentaryAdmin)
