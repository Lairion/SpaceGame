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
		"ships": ships,
		
	}
	ship_character = Ship.objects.filter(character_id=character,
			system_id=star)
	if len(ship_character)>0:
		status=False
		context.update({"character":character})	
	else:
		status=True
	context.update({"status": status})
	print(context)
	return render(request,"SpaceMap/system.html",context)

	