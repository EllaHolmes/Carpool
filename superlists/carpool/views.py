from django.shortcuts import render, redirect
from django.http import HttpResponse
from carpool.models import Rider, Driver
from datetime import date
from geopy.geocoders import Nominatim

debugging = False

# Create your views here.
def home_page(request):
    if 'newRider' in request.POST:
        user_= create_new_rider(request)
        user_.save()
    return render(request, 'base.html')

def new_user_page(request):
    if 'newDriver' in request.POST:
        user_ = create_new_driver(request)
        rider_list = find_riders_for_a_driver( user_)
        rider_list_empty = rider_list.count() == 0


        #if (debugging):
            #print(Rider.get_suitable_riders(user_))

        if(not rider_list_empty):
            return render( request, 'index.html', {'user_first_name': user_.nameFirst,
                                                'user_last_name': user_.nameLast,
                                                'user_start_loc': user_.start,
                                                'user_end_loc': user_.end,
                                                'user_date': user_.date,
                                                'list_of_riders': rider_list})
        else:
            return render(request, 'tempErrorPage.html')


    elif 'newRider' in request.POST:
        user_ = create_new_rider(request)
        #We have not made the page to send in this instance therefore it just saves. it should not send to index
        # driver_list = find_drivers_for_a_rider(user_)
        # return render( request, 'index.html', {'user_first_name': user_.nameFirst,
        #                                         'user_last_name': user_.nameLast,
        #                                         'user_start_loc': user_.start,
        #                                         'user_end_loc': user_.end,
        #                                         'user_date': user_.date,
        #                                         ''})
    else:
        print ("error: are you a rider or a driver?")




def create_new_driver(request):
    user_ = Driver()
    user_.create(
        request.POST['first_name_text'],
        request.POST['last_name_text'],
        request.POST['start_text'],
        request.POST['end_text'],
        request.POST['date_text']
    )

    #save the object
    user_.save()
    if (debugging):
        print(user_)
        print(Driver.objects.all())
    return user_

def create_new_rider(request):
    user_ = Rider()
    user_.create(
        request.POST['first_name_text'],
        request.POST['last_name_text'],
        request.POST['start_text'],
        request.POST['end_text'],
        request.POST['date_text']
    )

    #save the object
    user_.save()
    # driver_ =find_driver()
    return user_

def find_drivers_for_a_rider(user):
    if (debugging):
        return Driver.objects.all()
    else:
        # all_drivers = Driver.objects.all()
        filtered_drivers = Driver.objects.filter(date = user.date)[:5]
        for item in filtered_drivers:
            print (item.nameFirst)
        # q2 = q1.filter(end = "Chicago")[:5]
        return filtered_drivers


def find_riders_for_a_driver(user):
    if (debugging):
        return Rider.objects.all()
    else:
        filtered_riders = Rider.objects.filter(date = user.date
                                    ).filter(start__iexact = user.start
                                    ).filter(end__iexact = user.end)[:5]                           
        for item in filtered_riders:
            print (item.nameFirst + "Hello\n")
        return filtered_riders
