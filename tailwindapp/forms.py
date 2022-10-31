from django import forms

from .models import CommentPost, CommentProject

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentProject
        fields = ['name', 'email', 'body']
