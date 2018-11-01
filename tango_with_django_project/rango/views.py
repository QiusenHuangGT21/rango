from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from rango.models import Category, Page
# Create your views here.

def index(request):
	#return HttpResponse("Hello, world. You are at the rango page!\
	#<br/> <a href = '/rango/about/'> About </a>")
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	current_time = timezone.now()
	context_dict = {'categories': category_list,
					'pages': page_list,
					'current_time': current_time
					}
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
    return HttpResponse("Rango says this is the about page.\
	<br/> <a href = '/'>index</a>")

def show_category(request, category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category = category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None
	return render(request, 'rango/category.html', context_dict)