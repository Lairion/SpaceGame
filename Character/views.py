from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from .models import Character
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
		"title":"Character.html",
		"characters":characters
	}
	return render(request,
		"Character/character.html",
		context)



