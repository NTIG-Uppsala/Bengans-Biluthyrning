from seleniumbase import BaseCase
import os

startPage = "https://nikole-scheutz.github.io/"

class test_existens(BaseCase):
    def test_start(self):
        self.open(startPage)
        self.assert_text("This is Nikole Scheutz' website", "body")