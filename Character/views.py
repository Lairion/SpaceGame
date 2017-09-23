from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from .models import Ship,Character,Engine,Engine_ship,Laser,Laser_ship
# Create your views here.
@csrf_protect
def register_in_site_post(request):
	username = request.POST.get("user_name")
	e_mail = request.POST.get("e-mail")
	password = request.POST.get("password")
	print(username,e_mail,password)
	user = User.objects.create_user(username,e_mail,password)
	print(user)
	return HttpResponseRedirect("/login/")
def registration(request):
	return render(request,
		"Character/registration.html",
		{"title":"Registration"})

def login_site(request):

	if request.user.is_authenticated:
		return HttpResponseRedirect('/characters/')

	return render(request,
		"Character/login.html",
		{"title":"Login"})
@csrf_protect
def login_in_site(request):
	user_name = request.POST.get("user_name")
	password = request.POST.get("password")
	user = authenticate(request,username=user_name,password=password)
	print(user)
	if user is not None:
		login(request,user)
		return HttpResponseRedirect("/characters/")
	else:
		return HttpResponse("false")

def logout_in_site(request):
	logout(request)
	return HttpResponseRedirect("/login/")

def character_page(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/login/")
	print(dir(request.user))
	characters = Character.objects.filter(
		user_id=request.user)
	context = {
		"title":"Characters",
		"characters":characters
	}
	return render(request,"Character/characters.html",context)

def catch_defaul_parameters(request):
	player_ship_id = request.GET.get("player_id")
	enemy_ship_id = request.GET.get("enemy_id")
	player_ship_id = Ship.objects.get(id=int(player_ship_id))
	enemy_ship_id = Ship.objects.get(id=int(enemy_ship_id))
	request.session.__setitem__("Fight")
	request.session["Fight"] = {
		'round':"1",
		'player_ship': str(player_ship_id.id),
		'enemy_ship': str(enemy_ship_id.id)
	}
	return HttpResponseRedirect("/fight/")
def fight(request):
	player_ship_id = Ship.objects.get(id=int(request.session["player_ship"]))
	enemy_ship_id = Ship.objects.get(id=int(request.session["enemy_ship"]))
	context = {
		'player_ship':player_ship_id,
		'enemy_ship':enemy_ship_id,
		}
	return render(request,
		"Character/fight.html",
		context)


def character(request,id):
	character = Character.objects.get(id=int(id))
	ships = Ship.objects.filter(character_id=character)
	context = {
		"title":"Character",
		"character":character,
		"ships": ships
	}
	print(request.session.get("round"))
	return render(request,
		"Character/character.html",
		context)
def ship_interface(request,id):
	ship = Ship.objects.get(id=int(id))
	lasers = Laser_ship.objects.filter(ship_id=ship)
	engine = Engine_ship.objects.filter(ship_id=ship)
	context = {
		"title":"Ship",
		"ship":ship,
		"lasers": lasers,
		"engine": engine
	}
	request.session.__setitem__("round","1")
	print(request.session.get("round"))
	return render(request,
		"Character/ship_interface.html",
		context)




