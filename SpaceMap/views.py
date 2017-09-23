from django.shortcuts import render
from .models import StarSystem,Planet
from Character.models import Character,Ship
# Create your views here.
def space_view(request):
	star_systems = StarSystem.objects.all()
	print(request.user)
	context = {
		'title':"SpaceMap", 
		"SpaceSystems":star_systems
	}
	return render(request,"SpaceMap/space.html",context)
def system_view(request,id):
	star = StarSystem.objects.get(id=int(id))
	character = Character.objects.get(user_id=request.user,is_active=True)
	ships = Ship.objects.filter(system_id=star)
	planets = Planet.objects.filter(star_system=star)
	context = {
		'title':"System "+ star.name_system, 
		"Star": star,
		"Planets": planets,
		"ships": ships
	}
	try:
		ship_character = Ship.objects.get(character_id=character,
			system_id=star)
		status=False
		print(1)
		context.update({"status": status, "character":ship_character})	
	except:
		print(2)
		status=True
		context.update({"status": status})
	return render(request,"SpaceMap/system.html",context)

	