from django.db import models

class User(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)

class Calendar(models.Model):
	name = models.CharField(max_length = 30)
	user = models.ForeignKey(User)
	date = models.DateField()
	gift = models.TextField()
	gift_type = models.CharField(max_length = 30)
	opened = models.BooleanField(default = False)