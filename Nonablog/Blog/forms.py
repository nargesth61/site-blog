from .models import Post
from django import forms


class AddNewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields =('image','author','title','content','counted_views','category','status')
