from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

productPage = filePath + "english/products.html"  # Path to products.html

productList = [
    "Audi A6",
    "Renault Kadjar",
    "Kia Soul",
    "Subaru Outback",
    "Cadillac Escalade",
    "Mitsubishi Outlander",
    "Volvo XC40",
    "VW Polo",
    "Kia Carens"
]

class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(productPage)
        self.assert_title("Bengan's Car Rentals")

class products(BaseCase):
    def testProducts(self):
        self.open(productPage)
        # Looks for the items in productList
        for i in productList:
            self.assert_text(i)
