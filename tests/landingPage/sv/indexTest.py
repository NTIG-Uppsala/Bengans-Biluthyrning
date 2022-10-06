from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-20].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(startPage)
        self.assert_title("Bengans Biluthyrning")

    def testBackground(self):
        self.open(startPage)
        self.assert_element(".backgroundImage")

    def testButton(self):
        self.open(startPage)
        self.assert_element("#buttons a[href=\"jonkoping/sv/index.html\"]")
        self.assert_element("#buttons a[href=\"lulea/sv/index.html\"]")
