from seleniumbase import BaseCase
import os

startPage = "https://ntig-uppsala.github.io/Bengans-Biluthyrning/"

class company(BaseCase):
    def test_start(self):
        self.open(startPage)
        self.assert_text("Bengans Biluthyrning", "body")
    def test_title(self):
        self.open(startPage)
        self.assert_title("Bengans Biluthyrning")

#Loop function instead of creating multiple