from seleniumbase import BaseCase  #importing testing framework
import pathlib

startPage = "file:///" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/") + "index.html" #website url

basicInfoTexts = ["Fjällgatan 32H, 981 39 Jönköping", "Vardagar: 10-16", "Lördagar: 12-15", "Söndagar: Stängt", "0630-555-555", "info@<DOMÄN>"]

socialMedia = ["#facebook", "#twitter", "#instagram"]
socialLinks = ["https://sv-se.facebook.com/ntiuppsala/", "https://twitter.com/ntiuppsala", "https://www.instagram.com/ntiuppsala/"]

pictureIds = ["#bild1", "#bild2", "#bild3"]

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
            self.assert_text(i, "body") #Checks for all info in basicInfoTexts[]
    def testIcons(self):
        for i in range(len(socialMedia)):
            self.open(startPage)
            self.click(socialMedia[i]) #Checks that the icon link exists, and clicks if it does
            if(self.get_current_url() != socialLinks[i]): #Checks that links lead to the right place
                raise NameError(f"Failed at {socialMedia[i]}")

class imagesProducts(BaseCase):
    def testText(self):  
        self.open(startPage)        #self.open another page later
        for i in pictureIds:
            self.assert_element(f"img{i}") #Checks for the 3 images
        #check for products
        #check for logo in header
        self.assert_element("head > link[href=\"/images/favicon.ico\"][rel=\"icon\"]") #Checks for a link to favicon in head


# Överrubriker i backlogg är klasser, underrubrik är funktioner