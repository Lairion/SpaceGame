from django.shortcuts import render
from .models import StarSystem,Planet
# Create your views here.
def space_view(request):
	star_systems = StarSystem.objects.all()
	context = {
		'title':"SpaceMap", 
		"SpaceSystems":star_systems
	}
	return render(request,"SpaceMap/space.html",context)
def system_view(request,id):
	star = StarSystem.objects.get(id=int(id))
	planets = Planet.objects.filter(star_system=star)
	context = {
		'title':"SpaceMap", 
		"SpaceSystems":star_systems
	}
	return render(request,"SpaceMap/space.html",context)

	