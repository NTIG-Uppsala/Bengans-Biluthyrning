# based on https://github.com/jsoma/selenium-github-actions
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By

class CheckSiteAvailability(unittest.TestCase):
    """
        If the script fails in the first test 
        it means that the website isn't online and running
    """
    def setup(self):
        driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install() # installing the driver to memory

        chrome_options = Options() # 
        chrome_options.add_argument("--headless") # 

        self.browser = webdriver.Chrome(driver_path, options=chrome_options) # Initializes chrome driver from the local instance of chrome
        self.addCleanup(self.browser.quit) # close the browser when the tests are done

        self.website_url = "https://ntig-uppsala.github.io/bengans-biluthyrning/" # url to be used
        # self.website_url = "http://127.0.0.1:5500/src/" # url that will be used

    def test_page_title(self):
        self.browser.get(self.website_url)
        self.assertIn("Bengans Biluthyrning", self.browser.title)

    def test_page_text(self):
        self.browser.get(self.website_url)
        self.assertIn("Bengans Biluthyrning", self.browser.find_element(By.TAG_NAME, "body").text)

if __name__ == '__main__':      #runs all code in the test
    unittest.main(verbosity=69)  #how much info to be output to terminal