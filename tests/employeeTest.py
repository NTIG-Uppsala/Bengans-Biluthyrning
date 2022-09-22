from seleniumbase import BaseCase  # importing testing framework
import pathlib
import re

# To start the test, run "python -m pytest .\indexTest.py" in "\Bengans-Biluthyrning\tests"
# or "python -m pytest .\tests\indexTest.py" in "\Bengans-Biluthyrning"

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

productPage = filePath + "products.html"  # Path to products.html

employeePage = filePath + "employees.html" # Path to employees.html

emplyeeList = ["Anna Pettersson", "Fredrik Ortqvist", "Peter Johansson"]


class employees(BaseCase):
    def testNames(self):
        self.open(employeePage)
        for i in emplyeeList:
            self.assert_text(i)