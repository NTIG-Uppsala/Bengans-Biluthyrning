from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

productPage = filePath + "produkter.html"  # Path to products.html

productList = [
    ["audiA6","audiA6.jpg", "Audi A6", "Automat", "800 kr/dygn"], 
    ["renaultKadjar", None, "Renault Kadjar", "Automat", "450 kr/dygn"],
    ["kiaSoul", None, "Kia Soul", "Manuell", "400 kr/dygn"],
    ["subaruOutback","subaruOutback.jpg", "Subaru Outback", "Manuell", "300 kr/dygn"],
    ["cadillacEscalade","cadillacEscalade.jpg", "Cadillac Escalade", "Manuell", "500 kr/dygn"],
    ["mitsubishiOutlander","mitsubishiOutlander.jpg", "Mitsubishi Outlander", "Manuell", "450 kr/dygn"],
    ["volvoXC40","volvoXC40.jpg", "Volvo XC40", "Automat", "800 kr/dygn"],
    ["vwPolo","vwPolo.jpg", "VW Polo", "Manuell", "300 kr/dygn"],
    ["kiaCarens", None, "Kia Carens", "Manuell", "500 kr/dygn"]
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
            self.assert_text(i[2], "#"+i[0])
            self.assert_text(i[3], "#"+i[0])
            self.assert_text(i[4], "#"+i[0])
            if i[1] != None:
                self.assert_element("#"+i[0]+' .cardImage img[src="src/images/products/'+i[1]+'"]')


# for i in productList:
#     if i[1] != None:
#         print("#"+i[0]+' .cardImage[src='+i[1]+']')
