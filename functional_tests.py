from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Claires heard of a new to-do web app. She goes to the site
        # to check it out.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention the To-Do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She's prompted to enter a to-do item and test the app herself
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types in "Look for a post-office" into a text box
        inputbox.send_keys('Look for a post-office')

        # She hits enter, and upon doing so, the page updates and now
        # lists: "1: Look for a post-office"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Look for a post-office' for row in rows), "New to-do item did not appear in table"
        )

        # The text-box remains for her to input another item. She enters:
        # "Ask Kris to send over go-pro"
        self.fail('Finish the test!')

        # The page updates a second time and both her items are still
        # on the list

        # Claire notices that the site has generated a unique URL for her.
        # Along with explanatory text.

        # She visits the URL and notices her to-do list is saved and still there.

        # Satisfied, she goes back to sleep.
        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')