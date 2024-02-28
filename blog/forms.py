# 
#  FILE		      : forms.py
#  PROJECT		  : Django-blog
#  PROGRAMMER	  : Victor Barbosa
#  FIRST VERSION  : 2022-07-01
#  DESCRIPTION	  : This file contains the forms for the blog app.
# 



from django.forms import ModelForm
from blog.models import Commentary



# Comments form
class CommentForm(ModelForm):
    class Meta:
        model = Commentary
        exclude = ["post","date"]
        labels = {
            "author": "Your Name",
            "content": "Your Comment",
            
        }
        error_messages = {
            "author": {
                "required": "You must enter a name",
                "max_lenght": "Please enter a shorter name",
            },
            "content": {
                "required": "You must enter a comment",
                "max_lenght": "Please enter a shorter comment",
            },
        }