from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Character(models.Model):
	user_id = models.ForeignKey(User)
	name_character = models.CharField(max_length=100)
	level = models.IntegerField(default = 1)
	exp = models.IntegerField(default = 0)
	points = models.IntegerField(default= 0)
	image= models.ImageField(null=True, blank=True, upload_to='character_image/%Y/%m/%d')
	def __str__(self):
		return self.name_character
