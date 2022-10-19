from django import forms
from .models import Author, Post, Reply, Comment

class EntryForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["fullname", "bio"]

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "replies"]

# class UpAuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ["fullname", "bio", "profile_pic"]

