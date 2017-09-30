from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from .models import Ship,Character,Engine,Engine_ship,Laser,Laser_ship
import random
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
	parameters = {
		'round': 1,
		'player_ship': player_ship_id.id,
		'enemy_ship': enemy_ship_id.id,
		"status": "defence",
		"player_points":[0,0],
		"enemy_points":[0,0],
		"player_bonus": [0,0],
		"enemy_bonus": [0,0],
		"wait_result": False

	}
	request.session.__setitem__("Fight",parameters)

	return HttpResponseRedirect("/fight/")

def self_random(dice):
	result = random.randint(1,dice)
	if result == dice:
		result+=self_random(dice)
	return result

def attack(request):
	session = request.session["Fight"]
	player_ship_id = Ship.objects.get(id=int(session["player_ship"]))
	enemy_ship_id = Ship.objects.get(id=int(session["enemy_ship"]))
	session['player_points'][0] = self_random(6)
	session['player_points'][1] = self_random(player_ship_id.character_id.accurancy)
	session['enemy_points'][0] =self_random(6)
	session['enemy_points'][1] = self_random(enemy_ship_id.character_id.defence)
	session['player_bonus'][0] = session['player_points'][0]//6
	session['player_bonus'][1] = session['player_points'][1]//player_ship_id.character_id.accurancy
	session['wait_result'] = True
	request.session['Fight'] = session
	return HttpResponseRedirect("/fight/")
	# return HttpResponse('Thanks for your comment!')

def defence(request):
	session = request.session["Fight"]
	player_ship_id = Ship.objects.get(id=int(session["player_ship"]))
	enemy_ship_id = Ship.objects.get(id=int(session["enemy_ship"]))
	session['player_points'][0] = self_random(6)
	session['player_points'][1] = self_random(player_ship_id.character_id.defence)
	session['enemy_points'][0] =self_random(6)
	session['enemy_points'][1] = self_random(enemy_ship_id.character_id.accurancy)
	session['enemy_bonus'][0] = session['enemy_points'][0]//6
	session['enemy_bonus'][1] = session['enemy_points'][1]//player_ship_id.character_id.accurancy
	session['wait_result'] = True
	request.session['Fight'] = session
	return HttpResponseRedirect("/fight/")

def check_throws(attack,defence):
	if attack>defence:
		return True
	else:
		return False 
def catch_bonus(throw,points,bonus):
	a = points.index(int(throw))
	return bonus[a]

def choice_result(request):
	session = request.session["Fight"]
	player_throw = int(request.GET.get("throw"))
	enemy_throw = max(session['enemy_points'])
	if session['status'] == 'defence':

		enemy_ship = Ship.objects.get(id=int(session["enemy_ship"]))
		player_ship = Ship.objects.get(id=int(session["player_ship"]))
		enemy_is_successful = check_throws(enemy_throw,player_throw)
		if enemy_is_successful:
			lasers = Laser_ship.objects.filter(ship_id = enemy_ship)
			damage = sum([laser.power for laser in lasers])
			player_ship.armor -= damage + (damage * catch_bonus(enemy_throw,
				session['enemy_points'],
				session['enemy_bonus']))
			player_ship.save()
		session['status'] = 'attack'
	else:
		enemy_ship = Ship.objects.get(id=int(session["enemy_ship"]))
		player_ship = Ship.objects.get(id=int(session["player_ship"]))
		player_is_successful = check_throws(player_throw,enemy_throw)
		if player_is_successful:
			lasers = Laser_ship.objects.filter(ship_id = player_ship)
			damage = sum([laser.power for laser in lasers])
			enemy_ship.armor -= damage + (damage * catch_bonus(player_throw,
				session['player_points'],
				session['player_bonus']))
			enemy_ship.save()
		session['status'] = 'defence'
	session['wait_result'] = False
	request.session['Fight'] = session
	return HttpResponseRedirect("/fight/")
    


def buy_engine(request):
	url = request.GET.get("url")
	ship_id = request.GET.get("ship")
	engine_id = request.GET.get("engine")
	engine = Engine.objects.get(id=int(engine_id))
	ship = Ship.objects.get(id=int(ship_id))
	ship.character_id.buy_engine(engine)
	print(dir(request.get_full_path))
	print(request.get_full_path())
	return HttpResponseRedirect(url)


def fight(request):
	print("Fight here")
	print(request.session["Fight"])
	player_ship_id = Ship.objects.get(id=int(request.session["Fight"]["player_ship"]))
	enemy_ship_id = Ship.objects.get(id=int(request.session["Fight"]["enemy_ship"]))
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




