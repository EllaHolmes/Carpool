from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from carpool.views import home_page
from carpool.models import User

# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('base.html')
		self.assertEqual(response.content.decode(), expected_html)
		
	def test_can_save_user_info(self):
		first_user = User(nameFirst = "Mary", nameLast = "Jane", start = "New York", end = "Hampshire", date= "Today")
		
		first_user.text = 'First user'
		first_user.save()
		
		self.assertEqual(User.objects.all().count(), 1)
		
	def test_home_page_can_save_user(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['fname'] = 'A new user first name'
		
		response = home_page(request)
		
		self.assertEqual(User.objects.all().count(), 1)
		
	def test_home_page_can_redirect_and_use_data_base(self):
		pass
