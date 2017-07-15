from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	""" Form of creating Post """

	class Meta:
		model = Post
		fields = ('title', 'text', 'short_text', )
		