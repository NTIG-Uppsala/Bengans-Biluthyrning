from seleniumbase import BaseCase  #importing testing framework
import pathlib

startPage = "file:///" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/") + "index.html" #website url

basicInfoTexts = ["Fjällgatan 32H, 981 39 Jönköping", "Vardagar: 10-16", "Lördagar: 12-15", "Söndagar: Stängt", "0630-555-555", "info@<DOMÄN>"]

socialMedia = ["#facebook", "#twitter", "#instagram"]
socialLinks = ["https://sv-se.facebook.com/ntiuppsala/", "https://twitter.com/ntiuppsala", "https://www.instagram.com/ntiuppsala/"]

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
        for i in basicInfoTexts:
            self.assert_text(i, "body")
    def testIcons(self):
        for i in range(len(socialMedia)):
            self.open(startPage)
            self.assert_element(socialMedia[i])
            self.click(socialMedia[i])
            if(self.get_current_url() != socialLinks[i]):
                raise NameError(f"Failed at {socialMedia[i]}")

class imagesProducts(BaseCase):
    def testText(self):  
        pass
        #self.open another page
        #check for images
        #check for products
        #check for logo


# Överrubriker i backlogg är klasser, underrubrik är funktioner