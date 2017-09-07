from django.shortcuts import render
from .models import StarSystem,Planet
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
	print(request.user)
	planets = Planet.objects.filter(star_system=star)
	context = {
		'title':"System "+ star.name_system, 
		"Star": star,
		"Planets": planets
	}
	return render(request,"SpaceMap/system.html",context)

	