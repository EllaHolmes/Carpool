from django.shortcuts import render, redirect
from django.http import HttpResponse
from carpool.models import Rider, Driver

# Create your views here.
def home_page(request):
	if 'newRider' in request.POST:
		user_= create_new_rider(request)
		user_.save()
	return render(request, 'base.html')

def new_user_page(request):
    if 'newDriver' in request.POST:
        user_ = create_new_driver(request)
    elif 'newRider' in request.POST:
        user_ = create_new_rider(request)
    return render( request, 'index.html', {'user_first_name': user_.nameFirst,
                                            'user_last_name': user_.nameLast,
                                            'user_start_loc': user_.start,
                                            'user_end_loc': user_.end,
                                            'user_date': user_.date})


def create_new_driver(request):
    print ('I can drive')
    user_ = Driver.objects.create(nameFirst = request.POST['first_name_text'],
                                nameLast = request.POST['last_name_text'],
                                start = request.POST['start_text'],
                                end = request.POST['end_text'],
                                date = request.POST['date_text'])
    #save the object
    user_.save()
    return user_

def create_new_rider(request):
    print ('Im a new rider')
    user_ = Rider.objects.create(nameFirst = request.POST['first_name_text'],
                                nameLast = request.POST['last_name_text'],
                                start = request.POST['start_text'],
                                end = request.POST['end_text'],
                                date = request.POST['date_text'])
    #save the object
    user_.save()
    return user_
