from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
# Create your models here.

@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=16)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=16)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Book(models.Model): 
	book_name = models.CharField(max_length=128)
	number = models.DecimalField(max_digits=4, decimal_places=0)
	publish_date = models.DateTimeField()
	publish_edition = models.CharField(max_length=8)
	post_time = models.DateTimeField(auto_now=True)
	press = models.CharField(max_length=64)
	translater = models.CharField(max_length=32,blank=True)
	book_author = models.CharField(max_length=32)
	language = models.CharField(max_length=32)
	mobile_number = models.DecimalField(max_digits=11, decimal_places=0)
	tags = models.ManyToManyField(Tag,blank=True)
	email = models.EmailField(max_length=128)
	address = models.CharField(max_length=256)
	category = models.ManyToManyField(Category,blank=False)
	def __str__(self):
		return self.book_name
