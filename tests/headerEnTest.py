from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "english/index.html"  # Path to index.html

productPage = filePath + "english/products.html"  # Path to products.html

employeePage = filePath + "english/employees.html" # Path to employees.html

pages = [startPage, productPage, employeePage]


class header(BaseCase):
    def testName(self):
        # Find "Bengan's Car Rentals" in every header
        for i in pages:
            self.open(i)
            self.assert_text("Bengan's Car Rentals", "#header")

    def testMenu(self):
        # Find the menu links, in <nav> if a burger menu is clickable, otherwise in #menu
        for i in pages:
            self.open(i)
            try:
                self.click("label", timeout=1)
            except:
                # Activates if there is no burger menu
                self.assert_element("#menu a[href=\"products.html\"]")
                self.assert_element("#menu a[href=\"index.html\"]")
                self.assert_element("#menu a[href=\"employees.html\"]")
            else:
                # Activates if there is a burger menu
                self.assert_element("nav a[href=\"products.html\"]")
                self.assert_element("nav a[href=\"index.html\"]")
                self.assert_element("nav a[href=\"employees.html\"]")

    def testLogo(self):
        # Find logo in every header
        for i in pages:
            self.open(i)
            self.assert_element("#header [src=\"../src/images/svg/logo.svg\"]")
