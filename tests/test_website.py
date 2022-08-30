# Utgår ifrån https://github.com/jsoma/selenium-github-actions
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
        driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install() # installerar drivern i minnet

        chrome_options = Options() # 
        chrome_options.add_argument("--headless") # 

        self.browser = webdriver.Chrome(driver_path, options=chrome_options) # Initiliserar chrome drivern från den nerladdade
        self.addCleanup(self.browser.quit) # stäng webläsaren när testen är klar

        self.website_url = "https://ntig-uppsala.github.io/bengans-biluthyrning/" # Urln som kommer användas
        # self.website_url = "http://127.0.0.1:5500/src/" # Urln som kommer användas

    def test_page_title(self):
        self.browser.get(self.website_url)
        self.assertIn("Bengans Biluthyrning", self.browser.title)

    def test_page_text(self):
        self.browser.get(self.website_url)
        self.assertIn("Bengans Biluthyrning", self.browser.find_element(By.TAG_NAME, "body"))
    
        #self.assertIn(info_value, self.browser.find_element(By.TAG_NAME, "body").text)


if __name__ == '__main__':      #Kör igenom all kod i testet
    unittest.main(verbosity=69)  #Hur mycket information som ges av testerna
