# commentaries/forms.py
from django import forms
from .models import Thought


class ThoughtsListForm(forms.Form):
    class Meta(forms.ModelForm):
        model = Thought
        fields = ('title', 'reference', 'verseText', 'author', 'body',
                  'updated', 'status', 'keyWords')


class ThoughtCreationForm(forms.Form):
    class Meta(forms.ModelForm):
        model = Thought
        fields = ('title', 'body')


class ThoughtUpdateForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'reference', 'verseText', 'author', 'body',
                  'status', 'keyWords']