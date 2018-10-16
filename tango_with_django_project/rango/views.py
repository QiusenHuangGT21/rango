from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Hello, world. You are at the rango page!\
	<br/> <a href = '/rango/about/'> About </a>")

def about(request):
    return HttpResponse("Rango says this is the about page.")
