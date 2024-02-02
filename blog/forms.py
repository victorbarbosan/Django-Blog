
from django.forms import ModelForm
from blog.models import Commentary


                                # class ReviewForm(forms.Form):
                                #     user_name = forms.CharField(label="Your Name", max_length=50, error_messages={
                                #         "required": "Your name must not be empty!",
                                #         "max_length": "Please enter a shorter name!", 
                                #     })
                                #     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
                                #     rating = forms.IntegerField(min_value=1, max_value=10, )

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
            }
        }