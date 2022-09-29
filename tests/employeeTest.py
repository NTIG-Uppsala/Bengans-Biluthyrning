from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

productPage = filePath + "produkter.html"  # Path to products.html

employeePage = filePath + "personal.html"  # Path to employees.html

employeeList = ["Anna Pettersson", "Fredrik Örtqvist", "Peter Johansson"]

class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(productPage)
        self.assert_title("Bengans Biluthyrning")
        
class employees(BaseCase):
    def testNames(self):
        self.open(employeePage)
        for i in employeeList:
            self.assert_text(i)
