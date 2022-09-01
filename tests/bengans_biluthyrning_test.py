from seleniumbase import BaseCase  #importing testing framework
import os

start_page = "https://ntig-uppsala.github.io/Bengans-Biluthyrning/"  #website url

class company(BaseCase):
    def test_text(self):   #defining first test
        self.open(start_page) #opens the page in browser
        self.assert_text("Bengans Biluthyrning", "body")    #checks for "Bengans Biluthyrning" in body
    def test_title(self):
        self.open(start_page)
        self.assert_title("Bengans Biluthyrning")   #checks for "Bengans Biluthyrning" in title