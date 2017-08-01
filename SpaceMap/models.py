from django.db import models

# Create your models here.
class StarSystem(models.Model):
	"""docstring for ClassName"""
	pos_x=models.IntegerField()
	pos_y =models.IntegerField()
	size =models.FloatField()
	color = models.CharField(max_length=8)
	temp = models.FloatField()
	name_system =models.CharField(max_length=50)
	mass = models.FloatField()
	def __str__(self):
		return self.name_system
