from __future__ import unicode_literals
import bcrypt

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def login(self, post):
		user = self.filter(email=post.get('email')).first()
		if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
			return (True, user)
		return(False, 'notuser')

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	objects = UserManager()