from django import forms
from .models import Posts

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description', 'image', 'url']