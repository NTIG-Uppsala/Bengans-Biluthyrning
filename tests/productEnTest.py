from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

productPage = filePath + "EN/products.html"  # Path to products.html

productList = [
    ["audiA6","audiA6.jpg", "Audi A6", "Automatic", "800 SEK per day"], 
    ["renaultKadjar", None, "Renault Kadjar", "Automatic", "450 SEK per day"],
    ["kiaSoul", None, "Kia Soul", "Manual", "400 SEK per day"],
    ["subaruOutback","subaruOutback.jpg", "Subaru Outback", "Manual", "300 SEK per day"],
    ["cadillacEscalade","cadillacEscalade.jpg", "Cadillac Escalade", "Manual", "500 SEK per day"],
    ["mitsubishiOutlander","mitsubishiOutlander.jpg", "Mitsubishi Outlander", "Manual", "450 SEK per day"],
    ["volvoXC40","volvoXC40.jpg", "Volvo XC40", "Automatic", "800 SEK per day"],
    ["vwPolo","vwPolo.jpg", "VW Polo", "Manual", "300 SEK per day"],
    ["kiaCarens", None, "Kia Carens", "Manual", "500 SEK per day"]
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
            self.assert_text(i[2], "#"+i[0])
            self.assert_text(i[3], "#"+i[0])
            self.assert_text(i[4], "#"+i[0])
            if i[1] != None:
                self.assert_element("#"+i[0]+' .cardImage img[src="../src/images/products/'+i[1]+'"]')
