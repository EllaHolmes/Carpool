from django.shortcuts import render
from django.http import HttpResponse
from carpool.models import User

# Create your views here.
def home_page(request):
	if request.method == "POST":
		User(nameFirst = request).save()
		print("here")
		redirect('welcome/')
	#return render(request, 'base.html')
	
def new_user_page(request):
	render(request, 'base.html')
