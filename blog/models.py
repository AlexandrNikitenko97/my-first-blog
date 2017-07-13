from django.db import models
from django.utils import timezone


class Post(models.Model):
	"""Creating Post and methods for publish it"""

	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)	
	text = models.TextField()
	short_text = models.TextField(max_length = 500, blank = True, null = True)
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title	

