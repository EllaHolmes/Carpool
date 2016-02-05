from selenium import webdriver
import unittest
import carpool.views

class NewRiderVisitorTest(unittest.TestCase):

    find_ride_page_title = "Find a Ride"
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def enter_new_carpool_driver(self, name, start, end, date):
        pass

    def routes_are_found(self, startId, endId, date):
        #TODO implement a way to check the route
        return True

    def navigate_to_find_a_ride_page (self):
        #TODO loads find a ride page
        carpool.views.find_ride_page()
        pass

    def user_is_logged_in (self):
        #TODO check that user is logged in
        return True;

class RiderRevisitsTest(unittest.TestCase):
    def test_user_can_search_for_ride (self):
        #User opens up our website
        self.browser.get('http://localhost:8000')

        #Check that the user is logged in
        if (not self.user_is_logged_in()):
            self.fail("User is not logged in")

        #User navigates to find a ride page
        self.navigate_to_find_a_ride_page()

        #She enters in her information and presses enter
        self.user_login('username', 'password')

        #she is then redirected to a map that shows a list of people looking for a ride
        map_url = self.browser.current_url
        self.assertRegexMatches(map_url, '/map/.+')

        self.fail('Finish that test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
