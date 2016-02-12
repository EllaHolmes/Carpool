from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from carpool.views import home_page, new_user_page

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

    def test_home_page_saves_name_and_posts_to_new_page(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['first_name_text'] = 'new user name'

        response = new_user_page(request)

        self.assertEqual('new user name', response.content.decode())
