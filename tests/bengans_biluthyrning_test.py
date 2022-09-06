from seleniumbase import BaseCase  #importing testing framework
import pathlib

startPage = "file:///" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/") + "index.html" #website url

# listList = ["Random bullshit", "random stuff"]

class workingWebsite(BaseCase):
    def testText(self):   #defining first test
        self.open(startPage) #opens the page in browser
        self.assert_text("Bengans Biluthyrning", "body")    #checks for "Bengans Biluthyrning" in body
    def testTitle(self):
        self.open(startPage)
        self.assert_title("Bengans Biluthyrning")   #checks for "Bengans Biluthyrning" in title

class basicInformation(BaseCase):
    def testContactInfo(self):   
        self.open(startPage)
        self.assert_text("Adress", "body")
        self.assert_text("Öpettider", "body")
        self.assert_text("Telefonnummer", "body")
        self.assert_text("Mail", "body")
    def testIcons(self):
        self.open(startPage)
        self.is_element_present("#twitter", by="css selector")
        self.click("#twitter", by="css selector", timeout=None, delay=0, scroll=True)
        self.get_current_url()
        self.open(startPage)
        self.is_element_present("#facebook", by="css selector")
        self.click("#facebook", by="css selector", timeout=None, delay=0, scroll=True)
        self.get_current_url()
        self.open(startPage)
        self.is_element_present("#instagram", by="css selector")
        self.click("#instagram", by="css selector", timeout=None, delay=0, scroll=True)
        self.get_current_url()

class imagesProducts(BaseCase):
    def testText(self):  
        pass
        #self.open another page
        #check for images
        #check for products
        #check for logo


# Överrubriker i backlogg är klasser, underrubrik är funktioner