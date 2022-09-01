from seleniumbase import BaseCase
import os

startPage = "https://ntig-uppsala.github.io/Bengans-Biluthyrning/"

class company(BaseCase):
    def test_start(self):
        self.open(startPage)
        self.assert_text("Bengans Biluthyrning", "body")