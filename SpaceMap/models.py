from django.db import models

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
	pos_x=models.IntegerField()
	pos_y=models.IntegerField()
	size =models.FloatField(null=True, blank=True)
	color = models.CharField(max_length=8, choices=STAR_COLORS)
	temp = models.FloatField(null=True, blank=True)
	name_system =models.CharField(max_length=50)
	mass = models.FloatField(null=True, blank=True)
	def __str__(self):
		return self.name_system
