from django.db import models
from django.utils import timezone

class Post(models.Model):
	
	author = models.ForeignKey('auth.User') #this is a link to another model
	title  = models.CharField(max_length = 200)
	text   = models.TextField()
	created_date   = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	image_post = models.FileField(upload_to = "blog/uploads/postagem",blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Color(models.Model):

	name = models.CharField(max_length = 20)
	hex_value = models.CharField(max_length = 9)

	def publish(self):
		self.save()

	def __str__(self):
		return self.name

class Cat(models.Model):

	name = models.CharField(max_length = 20)
	status = models.CharField(max_length = 20)
	primary_color = models.ForeignKey(Color, related_name = '+', default = 1)
	second_color  = models.ForeignKey(Color, related_name = '+', default = 1)

	def publish(self):
		self.save()

	def __str__(self):
		return self.name