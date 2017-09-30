from django.shortcuts import render
from .models import StarSystem,Planet,City
from Character.models import Character,Ship,Laser,Engine
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
    return render(request,"SpaceMap/system.html",context)

def planet_view(request,id):
    planet = Planet.objects.get(id=int(id))
    character = Character.objects.get(user_id=request.user,is_active=True)
    ships = Ship.objects.filter(planet_id=planet)
    cities = City.objects.filter(planet=planet)
    ship_character = Ship.objects.filter(character_id=character,
            planet_id=planet)
    context = {
        'title':"Planet"+ planet.name_planet, 
        "planet": planet,
        "cities": cities,
        "ships": ships,
        
    }
    if len(ship_character)>0:
        status=False
        context.update({"character":character}) 
    else:
        status=True
    context.update({"status": status})

    return render(request,"SpaceMap/planet.html",context)
def city_view(request,id):
    city = City.objects.get(id=int(id))
    character = Character.objects.get(user_id=request.user,is_active=True)
    ships = Ship.objects.filter(city_id=city)
    lasers = Laser.objects.filter(city_id=city)
    engines = Engine.objects.filter(city_id=city)
    ship_character = Ship.objects.filter(character_id=character)
    print(ship_character)
    context = {
        'title':"City"+ city.name_city, 
        "city": city,
        "lasers": lasers,
        "engines":engines,
        "ships": ships,
        "ship_character":ship_character[0]      
    }
    if len(ship_character)>0:
        status=False
        context.update({"character":character}) 
    else:
        status=True
    context.update({"status": status})

    return render(request,"SpaceMap/city.html",context)
    