from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'base.html')

def find_ride_page(request):
	return render(request, 'find/index.html')

def new_user_choice(request):
	return render(request, 'choice/index.html')