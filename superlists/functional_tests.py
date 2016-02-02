from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
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

    def test_user_can_search_for_ride (self):
        #User opens up our website
        self.browser.get('http://localhost:8000')

        #User navigates to find a ride page
        self.navigate_to_find_a_ride_page()

        #User sees title page "Find a Ride"
        self.assertIn(find_ride_page_title, self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(find_ride_page_title, header_text)

        #She is invited to enter in her name, start location, end location, and date
        inputName = self.browser.find_element_by_id('id_user')
        self.assertEqual(
            inputname.get_attribute('placeholder'),
            'Enter First and Last name'
        )

        inputStart = self.browser.find_element_by_id('id_start')
        self.assertEqual(
            inputStart.get_attribute('placeholder'),
            'Start Location'
        )

        inputEnd = self.browser.find_element_by_id('id_end')
        self.assertEqual(
            inputEnd.get_attribute('placeholder'),
            'End Location'
        )

        inputDate = self.browser.find_element_by_id('id_date')
        self.assertEqual(
            inputDate.get_attribute('placeholder'),
            'Travel Date'
        )

        #She enters in her information and presses enter
        self.enter_new_carpool_driver('Mary Lyon', 'South Hadley, MA', 'Amherst, MA', '1,1,2017')

        #she is then redirected to a map that shows a list of people looking for a ride
        map_url = self.browser.current_url
        self.assertRegexMatches(map_url, '/map/.+')

        self.fail('Finish thet test!')

    def test_user_can_enter_in_travel_plans(self):
        #User opens up our website
        self.browser.get('http://localhost:8000')

        #User sees our awesome title page and header mention Carpool
        self.assertIn('Carpool', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Carpool', header_text)

        #She is invited to enter in her name, start location, end location, and date
        inputName = self.browser.find_element_by_id('id_user')
        self.assertEqual(
            inputname.get_attribute('placeholder'),
            'Enter First and Last name'
        )

        inputStart = self.browser.find_element_by_id('id_start')
        self.assertEqual(
            inputStart.get_attribute('placeholder'),
            'Start Location'
        )

        inputEnd = self.browser.find_element_by_id('id_end')
        self.assertEqual(
            inputEnd.get_attribute('placeholder'),
            'End Location'
        )

        inputDate = self.browser.find_element_by_id('id_date')
        self.assertEqual(
            inputDate.get_attribute('placeholder'),
            'Travel Date'
        )

        #She enters in her information and presses enter
        self.enter_new_carpool_driver('Mary Lyon', 'South Hadley, MA', 'Amherst, MA', '1,1,2017')

        #she is then redirected to a map that shows a list of people looking for a ride
        map_url = self.browser.current_url
        self.assertRegexMatches(map_url, '/map/.+')

        self.fail('Finish thet test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
