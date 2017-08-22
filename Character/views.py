from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.
def register_in_site_post(request):

	username = request.GET.get("user_name")
	e_mail = request.GET.get("e-mail")
	password = request.GET.get("password")
	User.objects.create_user(username,e_mail,password)
	return HttpResponseRedirect("/login/")
def registration(request):
	return render(request,
		"Character/registration.html",
		{"title":"Registration"})
def login(request):
	return render(request,
		"Character/login.html",
		{"title":"Login"})
def character_page(request):
	return render(request,
		"Character/character.html",
		{"title":"Character.html"})



