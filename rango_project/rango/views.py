from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Ayy lmao welcome to the thunderdome")
