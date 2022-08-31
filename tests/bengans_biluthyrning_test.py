from seleniumbase import BaseCase
import os

startPage = "https://NTIG.github.bengans whatever/" #fix

class company(BaseCase):
    def test_start(self):
        self.open(startPage)
        self.assert_text("Bengans Biluthyrning", "body")