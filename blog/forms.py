from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	""" Form of creating Post """

	class Meta:
		model = Post
		fields = ('title', 'text', 'short_text', )
		

class CommentForm(forms.ModelForm):
	""" Form of creating Comment """

	class Meta:
	    model = Comment
	    fields = ('author', 'text',)