from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home_page():
    pass

def find_ride_page():
	template = loader.get_template('carpool/find/index.html')
	return HttpResponse(template.render(context))