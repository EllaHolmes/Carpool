from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def enter_new_carpool_driver(self, name, start, end, date):
        pass

    def test_user_can_enter_in_travel_plans(self):
        #User opens up our website
        self.browser.get('http://localhost:8000')

        #User sees our awesome title page and header mention Carpool
        self.assertIn('Carpool', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Carpool', header_text)

        #She is invited to enter in her name, start location, end location, and date
        inputName = self.browser.find_element_by_id('id_name')
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
