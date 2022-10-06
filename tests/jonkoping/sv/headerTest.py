from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-18].replace("\\", "/")

startPage = filePath + "jonkoping/sv/index.html"  # Path to index.html

productPage = filePath + "jonkoping/sv/produkter.html"  # Path to products.html

employeePage = filePath + "jonkoping/sv/personal.html" # Path to employees.html

pages = [startPage, productPage, employeePage]


# maybe needs fixing
startPageEN = "index.html"  # Path to index.html

productPageEN = "products.html"  # Path to products.html

employeePageEN = "staff.html" # Path to employees.html

pagesEN = [startPageEN, productPageEN, employeePageEN]


class header(BaseCase):
    def testName(self):
        # Find "Bengans Biluthyrning" in every header
        for i in pages:
            self.open(i)
            self.assert_text("Bengans Biluthyrning", "#header")

    def testMenu(self):
        # Find the menu links, in <nav> if a burger menu is clickable, otherwise in #menu
        for i in pages:
            self.open(i)
            try:
                self.click("label", timeout=1)
            except:
                # Activates if there is no burger menu
                self.assert_element("#menu a[href=\"produkter.html\"]")
                self.assert_element("#menu a[href=\"index.html\"]")
                self.assert_element("#menu a[href=\"personal.html\"]")
            else:
                # Activates if there is a burger menu
                self.assert_element("nav a[href=\"produkter.html\"]")
                self.assert_element("nav a[href=\"index.html\"]")
                self.assert_element("nav a[href=\"personal.html\"]")

    def testLogo(self):
        # Find logo in every header
        for i in pages:
            self.open(i)
            self.assert_element("#header [src=\"../../src/images/svg/logo.svg\"]")

    
    def testbutton(self):
        for i in range(len(pages)):
            self.open(pages[i])
            try:
                self.click("label", timeout=5)
            except:
                # Activates if there is no burger menu
                self.assert_element('#menu a[href=\"../en/'+pagesEN[i]+'\"]')
            else:
                # Activates if there is a burger menu
                self.assert_element('nav a[href=\"../en/'+pagesEN[i]+'\"]')