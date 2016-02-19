from django.shortcuts import render, redirect
from django.http import HttpResponse
from carpool.models import User

# Create your views here.
def home_page(request):
    return render(request, 'base.html')

def new_user_page(request):
    #gets the name from the request
    #creaet object from the name
    user_ = User.objects.create(nameFirst = request.POST['first_name_text'],
                                nameLast = request.POST['last_name_text'],
                                start = request.POST['start_text'],
                                end = request.POST['end_text'],
                                date = request.POST['date_text'])
    #save the object
    user_.save()
    print("in the new user page")
    # return redirect('/user/%s/' % new_user_name)
    return render( request, 'index.html', {'user_first_name': user_.nameFirst,
                                            'user_last_name': user_.nameLast,
                                            'user_start_loc': user_.start,
                                            'user_end_loc': user_.end,
                                            'user_date': user_.date})
