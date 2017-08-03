from django.shortcuts import render
from .models import StarSystem
# Create your views here.
def space_view(request):
	star_systems = StarSystem.objects.all()
	context = {
		'title':"SpaceMap", 
		"SpaceSystems":star_systems
	}
	return render(request,"SpaceMap/space.html",context)

	