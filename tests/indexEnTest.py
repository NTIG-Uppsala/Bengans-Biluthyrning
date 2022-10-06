from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "EN/index.html"  # Path to english index.html

class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(startPage)
        self.assert_title("Bengan's Car Rentals")

    def testBackground(self):
        self.open(startPage)
        self.assert_element(".backgroundImage")

    def testSlogan(self):
        self.open(startPage)
        self.assert_text("Nice Cars")
        self.assert_text("Nicer Prices")

    def testButton(self):
        self.open(startPage)
        self.assert_element(".main a[href=\"products.html\"]")