"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from carpool import views
from carpool.views import new_user_choice
from carpool.views import driver_home_page
from carpool.views import current_datetime
from carpool.views import process_driver
from carpool.views import test_form
from carpool.views import get_name

urlpatterns = [
    url(r'^$', views.home_page, name = 'home'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^new/$', new_user_choice, name = "new"),
    url(r'^driver/$', driver_home_page, name ="driver"),
    url(r'^process/$', process_driver, name ="process_driver"),
    url(r'^test/$', current_datetime, name = "test"),
    url(r'^form/$', test_form, name = "test_form"),
    url(r'^your-name/$', get_name, name = "your_name"),
    url(r'^thanks/$', get_name, name = "your_name")
]
