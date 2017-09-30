from django.db import models
from django.urls import reverse
# Create your models here.
class StarSystem(models.Model):
	"""docstring for ClassName"""
	STAR_COLORS = (
		("#ff0000","Red"),
		('#ffff66','Yellow'),
		('#66ffff','Blue',),
		('#ff66cc','Purpul'),
		('#ccff99','Green')
		)
	pos_x= models.IntegerField()
	pos_y= models.IntegerField()
	size = models.FloatField(null=True, blank=True)
	color = models.CharField(max_length=8, choices=STAR_COLORS)
	temp = models.FloatField(null=True, blank=True)
	name_system =models.CharField(max_length=50)
	mass = models.FloatField(null=True, blank=True)
	def __str__(self):
		return self.name_system
	def get_absolute_url(self):
		return reverse("Space:system_map", kwargs={"id": self.id})

class Planet(models.Model):
	star_system = models.ForeignKey(StarSystem)
	name_planet = models.CharField(max_length = 50)
	inhabited = models.BooleanField(default=False)
	atmosphere = models.BooleanField(default=False)
	distance = models.FloatField()
	diameter = models.FloatField()
	def __str__(self):
		return self.name_planet
	def get_absolute_url(self):
		return reverse("Space:planet_view", kwargs={"id": self.id})
class City(models.Model):
	CITY_STATUS = (
		("Vilage","Vilage"),
		("Town","Town"),
		("City","City")
		) 
	planet = models.ForeignKey(Planet)
	name_city = models.CharField(max_length=50)
	inhabited = models.BooleanField(default=True)
	space_port = models.BooleanField(default=True)
	population = models.IntegerField(default=0)
	city_status = models.CharField(max_length=7, 
		choices=CITY_STATUS, 
		default="Vilage" )
	def __str__(self):
		return self.name_city
	def get_absolute_url(self):
		return reverse("Space:city_view", kwargs={"id": self.id})


	
		


		
