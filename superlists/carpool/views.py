from django.shortcuts import render, redirect
from django.http import HttpResponse
from carpool.models import User

# Create your views here.
def home_page(request):
    # if request.method == "POST":
    #     print ("in home_page")
    #     return redirect('/user/')
        # return HttpResponse(request.POST['first_name_text'])
    return render(request, 'base.html')

def new_user_page(request):
    print ("in user_page")
    new_user_name = request.POST['first_name_text']
    print (new_user_name)
    user_ = User.objects.create(nameFirst = new_user_name)
    return render(request, 'index.html')
    # return HttpResponse(request.POST['first_name_text'])
