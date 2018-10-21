from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from rango.models import Category
# Create your views here.

def index(request):
	#return HttpResponse("Hello, world. You are at the rango page!\
	#<br/> <a href = '/rango/about/'> About </a>")
	category_list = Category.objects.order_by('-likes')[:5]
	current_time = timezone.now()
	context_dict = {'categories': category_list,
					'current_time': current_time
					}
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
    return HttpResponse("Rango says this is the about page.\
	<br/> <a href = '/'>index</a>")
