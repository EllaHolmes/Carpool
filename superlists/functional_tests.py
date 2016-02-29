from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import carpool.views
from django.conf import settings
from carpool.models import User



class NewDriverVisitorTest(unittest.TestCase):

    find_ride_page_title = "Find a Ride"
    settings.configure()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()



    def enter_new_carpool_driver(self, firstName, lastName, startLocation, endLocation,date):
        inputFirstName = self.browser.find_element_by_id('id_first_name')
        inputLastName = self.browser.find_element_by_id('id_last_name')
        inputStart = self.browser.find_element_by_id('id_start')
        inputEnd = self.browser.find_element_by_id('id_end')
        inputDate = self.browser.find_element_by_id('id_date')
        inputFirstName.send_keys(firstName)
        inputLastName.send_keys(lastName)
        inputStart.send_keys(startLocation)
        inputEnd.send_keys(endLocation)
        inputDate.send_keys(date)
        enterButton = self.browser.find_element_by_id('id_new_driver_btn')
        enterButton.send_key(Keys.ENTER)

    def enter_new_carpool_rider(self, firstName, lastName, startLocation, endLocation,date):
        inputFirstName = self.browser.find_element_by_id('id_first_name')
        inputLastName = self.browser.find_element_by_id('id_last_name')
        inputStart = self.browser.find_element_by_id('id_start')
        inputEnd = self.browser.find_element_by_id('id_end')
        inputDate = self.browser.find_element_by_id('id_date')
        inputFirstName.send_keys(firstName)
        inputLastName.send_keys(lastName)
        inputStart.send_keys(startLocation)
        inputEnd.send_keys(endLocation)
        inputDate.send_keys(date)
        enterButton = self.browser.find_element_by_id('id_new_rider_btn')
        enterButton.send_key(Keys.ENTER)


    def test_user_can_enter_in_travel_plans(self):
        #User opens up our website
        self.browser.get('http://localhost:8000')

        #User sees our awesome title page and header mention Carpool
        self.assertIn('Carpool', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Carpool', header_text)

        #She is invited to enter in her name, start location, end location
        inputFirstName = self.browser.find_element_by_id('id_first_name')
        self.assertEqual(
            inputFirstName.get_attribute('placeholder'),
            'First Name'
        )

        inputLastName = self.browser.find_element_by_id('id_last_name')
        self.assertEqual(
            inputLastName.get_attribute('placeholder'),
            'Last Name'
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

        #She enters in her information and presses enter
        # self.enter_new_carpool_driver('Mary', 'Lyon', 'South Hadley, MA', 'Amherst, MA', '1/1/1')

        # name = self.browser.find_element_by_id('id_first_name')

        # self.assertEqual('Mary', name)

        # #she is then redirected to a map that shows a list of people looking for a ride
        # map_url = self.browser.current_url
        # self.assertRegexMatches(map_url, '/map/.+')

        self.fail('Finish thet test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
