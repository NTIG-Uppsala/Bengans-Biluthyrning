from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

productPage = filePath + "produkter.html"  # Path to products.html

productList = [
    ["audiA6","audiA6.jpg", "Audi A6", "Automat", "800"], 
    ["renaultKadjar","renaultKadjar.jpg", "Renault Kadjar", "Automat", "450"],
    ["kiaSoul","kiaSoul.jpg", "Kia Soul", "Manuell", "400"],
    ["subaruOutback","subaruOutback.jpg", "Subaru Outback", "Manuell", "300"],
    ["cadillacEscalade","cadillacEscalade.jpg", "Cadillac Escalade", "Manuell", "500"],
    ["mitsubishiOutlander","mitsubishiOutlander.jpg", "Mitsubishi Outlander", "Manuell", "450"],
    ["volvoXC40","volvoXC40.jpg", "Volvo XC40", "Automat", "800"],
    ["vwPolo","vwPolo.jpg", "VW Polo", "Manuell", "300"],
    ["kiaCarens","kiaCarens.jpg", "Kia Carens", "Manuell", "500"]
]


class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(productPage)
        self.assert_title("Bengans Biluthyrning")

class products(BaseCase):
    def testProducts(self):
        self.open(productPage)
        # Looks for the items in productList
        for i in productList:
            self.assert_element(i)

for i in productList:
    print(i)
