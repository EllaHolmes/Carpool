from django.shortcuts import render
from django.http import HttpResponse
from .forms import DriverForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template
from django.template import Context
import datetime
from .forms import NameForm
from .forms import PostForm

# Create your views here.
def home_page(request):
    return render(request, 'base.html')

def find_ride_page(request):
	return render(request, 'find/index.html')

def new_user_choice(request):
	return render(request, 'choice/index.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def driver_home_page(request):
	print("this is kind of working")
	return render (request, 'driver/index.html')

def test_form(request):
	return render(request, 'form.html')

#From https://docs.djangoproject.com/en/1.9/topics/forms/
@ensure_csrf_cookie
@csrf_protect
def process_driver(request):
	print("this is working")
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = DriverForm(request.POST)
		print(form.is_bound)
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			return HttpResponseRedirect('/driver/')

    # if a GET (or any other method) we'll create a blank form
	else:
		print("fell through")
		form = DriverForm()
		return render(request, 'base.html', {'form' : form})
		#http://stackoverflow.com/questions/8089224/csrf-token-missing-or-incorrect
		return render_to_response("base.html", {'form' : form}, context_instance = RequestContext(request))

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def post_form(request):
	form = PostForm()
	return render(request, 'postform.html', {'form': form})