from selenium import webdriver
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
        self.fail('Finish the test!')

        # She's prompted to enter a to-do item and test the app herself

        # She types in "Look for a post-office" into a text box

        # She hits enter, and upon doing so, the page updates and now
        # lists: "1: Look for a post-office"

        # The text-box remains for her to input another item. She enters:
        # "Ask Kris to send over go-pro"

        # The page updates a second time and both her items are still
        # on the list

        # Claire notices that the site has generated a unique URL for her.
        # Along with explanatory text.

        # She visits the URL and notices her to-do list is saved and still there.

        # Satisfied, she goes back to sleep.
        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')