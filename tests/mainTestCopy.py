from seleniumbase import BaseCase  # importing testing framework
import pathlib

# To start the test, run "python -m pytest .\mainTest.py" in "\Bengans-Biluthyrning\tests"
# or "python -m pytest .\tests\mainTest.py" in "\Bengans-Biluthyrning"

# Find file path and prepare formatting
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

productPage = filePath + "products.html"  # Path to products.html

class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(startPage)
        self.assert_title("Bengans Biluthytsdrdstddtrning")
    


# Categories in the backlog are represented as classes, every item in the backlog has its own test
