from django.core.management.base import BaseCommand, CommandError
from SpaceMap.models import StarSystem
import random

class Command(BaseCommand):
	help = 'This command Create Galaxy map'

	def add_arguments(self, parser):
		parser.add_argument('count_iter', nargs='+', type=int)
		

	def handle(self,*args,**options):
		colors = []
		for i in StarSystem.STAR_COLORS:
			colors.append(i[0])
		name_system = ["Centavre",
			"San",
			"Amega",
			"Shakuras",
			"Aur",
			"Char",
			"Mebyus",
			"Gipirion",
			"Tiberium"
			]
		def check_list_name():
			value = random.choice(name_system)+str(random.randint(1,100))
			if StarSystem.objects.filter(name_system=value):
				return check_list_name()
			return value
		def check_list_position():
			values = [random.randint(1,2000),random.randint(1,2000)]
			if StarSystem.objects.filter(pos_x=values[0],pos_y=values[1]):
				return check_list_position()
			return values
		for i in range(options["count_iter"][0]):
			values = check_list_position()
			a = StarSystem(
				name_system=check_list_name(),
				pos_x=values[0],
				pos_y=values[1],
				color=random.choice(colors)
				)
			a.save()

				