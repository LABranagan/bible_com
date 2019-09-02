# commentaries/forms.py
from django import forms
from .models import Post


class PostCreationForm(forms.Form):
    class Meta(forms.ModelForm):
        model = Post
        fields = ('title', 'body')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'reference', 'body']