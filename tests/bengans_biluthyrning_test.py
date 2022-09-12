from seleniumbase import BaseCase  #importing testing framework
import pathlib

# To start the test, run "python -m pytest .\bengans_biluthyrning_test.py" in "\Bengans-Biluthyrning\tests"
# or "python -m pytest .\tests\bengans_biluthyrning_test.py" in "\Bengans-Biluthyrning"

startPage = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/") + "index.html" # Find location of index.html and prepare formatting

basicInfoTexts = ["Fjällgatan 32H, 981 39 Jönköping", "Vardagar: 10-16", "Lördagar: 12-15", "Söndagar: Stängt", "0630-555-555", "info@<DOMÄN>"] # Basic info to test for

socialMediaPaths = ["src/images/facebook.svg", "src/images/twitter.svg", "src/images/instagram.svg"] # Paths for different social media .svg imgs
socialLinks = ["https://sv-se.facebook.com/ntiuppsala/", "https://twitter.com/ntiuppsala", "https://www.instagram.com/ntiuppsala/"] # Relevant social media links

picturePaths = ["src/images/bild1.jpg", "src/images/bild2.jpg", "src/images/bild3.jpg"] # Paths for the images

productList = ["Audi A6", "Renault Kadjar", "Kia Soul", "Subaru Outback", "Caddilac Escalade", "Mitshubichi Outlander", "Volvo XC40", "VW Polo", "Kia Carens"] # List of products

class workingWebsite(BaseCase):
    def testText(self):
        self.open(startPage) # Open the page in browser
        self.assert_text("Bengans Biluthyrning", "body") # Check for "Bengans Biluthyrning" in body
    def testTitle(self):
        self.open(startPage)
        self.assert_title("Bengans Biluthyrning") # Check for "Bengans Biluthyrning" in title

class basicInformation(BaseCase):
    def testContactInfo(self):   
        self.open(startPage)
        for i in basicInfoTexts:
            self.assert_text(i, "body") # Check for all info in basicInfoTexts[]
    def testIcons(self):
        for i in range(len(socialMediaPaths)):
            self.open(startPage)
            self.click(f"[src=\"{socialMediaPaths[i]}\"]") # Check that the icon link exists, and clicks if it does
            if(self.get_current_url() != socialLinks[i]): # Checks that links lead to the right place
                raise NameError(f"Failed at {socialMediaPaths[i]}")

class imagesAndProducts(BaseCase):
    def testImages(self):  
        self.open(startPage)        # self.open another page later
        for i in picturePaths:
            self.assert_element(f"img[src=\"{i}\"]") # Check for the 3 images by path
    def testProducts(self):
        self.open(startPage)        # self.open another page later
        for i in productList:
            self.assert_text(i, "body") # Check for products
    def testLogo(self):
        self.open(startPage)
        # It is not possible to test for the content of <link>s, therefore we have decided to treat the favicon like a page design, untestable and therefore passed by default.
        # self.assert_element("head > link[sizes=\"32x32\"][href=\"src/images/icons/favicon-32x32.png\"]") #Checks for a link to 32x32 favicon in head
        self.assert_element("img[src=\"src/images/logo.svg\"]") # Check for an image with the ID #logo
        # Repeat for all pages once we add more


# Categories in the backlog are represented as classes, every item in the backlog has its own test