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
class Ship(models.Model):
	"""docstring for Ship"""
	SHIP_CLASS = (("DR","DRAGUN"),("HS","HeavyShip"),("MD","Medical"))
	name_ship = models.CharField(max_length=100)
	ship_class = models.CharField(max_length=3,choices=SHIP_CLASS,default="DR") 
	armor = models.IntegerField(default=400)
class Engine():
	"""docstring for Engine"""
	price = models.DecimalField(max_digits=19, decimal_places=2)
	name_engine = models.CharField(max_length=100)
	power = models.IntegerField(default=1000)
	durability = models.IntegerField(default=1000)
		

