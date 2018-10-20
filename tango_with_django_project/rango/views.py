from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.

def index(request):
	#return HttpResponse("Hello, world. You are at the rango page!\
	#<br/> <a href = '/rango/about/'> About </a>")
	
	current_time = timezone.now()
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!", \
					'current_time': current_time}
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
    return HttpResponse("Rango says this is the about page.\
	<br/> <a href = '/'>index</a>")
