from seleniumbase import BaseCase  # importing testing framework
import pathlib

# To start the test, run "python -m pytest .\mainTest.py" in "\Bengans-Biluthyrning\tests"
# or "python -m pytest .\tests\mainTest.py" in "\Bengans-Biluthyrning"

# Find file path and prepare formatting
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

productPage = filePath + "products.html"  # Path to products.html

basicInfoTexts = ["Fjällgatan 32H, 981 39 Jönköping", "Vardagar: 10-16", "Lördagar: 12-15",
                  "Söndagar: Stängt", "0630-555-555", "info@<DOMÄN>"]  # Basic info to test for

socialMediaPaths = ["src/images/svg/facebookIcon.svg", "src/images/svg/twitterIcon.svg",
                    "src/images/svg/instagramIcon.svg"]  # Paths for different social media .svg imgs
socialLinks = ["https://sv-se.facebook.com/ntiuppsala/", "https://twitter.com/ntiuppsala",
               "https://www.instagram.com/ntiuppsala/"]  # Relevant social media links

'''
picturePaths = ["src/images/bild1.jpg", "src/images/bild2.jpg",
                "src/images/bild3.jpg"]  # Paths for the images
'''

productList = ["Audi A6", "Renault Kadjar", "Kia Soul", "Subaru Outback", "Cadillac Escalade",
               "Mitsubishi Outlander", "Volvo XC40", "VW Polo", "Kia Carens"]  # List of products


class workingWebsite(BaseCase):
    def testText(self):
        self.open(startPage)  # Open the page in browser
        # Check for "Bengans Biluthyrning" in body
        self.assert_text("Bengans Biluthyrning", "body")

    def testTitle(self):
        self.open(startPage)
        # Check for "Bengans Biluthyrning" in title
        self.assert_title("Bengans Biluthyrning")


class basicInformation(BaseCase):
    def testContactInfo(self):
        self.open(startPage)
        for i in basicInfoTexts:
            # Check for all info in basicInfoTexts[]
            self.assert_text(i, "body")

    def testIcons(self):
        for i in range(len(socialMediaPaths)):
            self.open(startPage)
            # Check that the icon link exists, and clicks if it does
            self.click(f"[src=\"{socialMediaPaths[i]}\"]")
            # Checks that links lead to the right place
            if (self.get_current_url() != socialLinks[i]):
                raise NameError(f"Failed at {socialMediaPaths[i]}")


class imagesAndProducts(BaseCase):
    '''
    def testImages(self):
        self.open(startPage)        # self.open another page later
        for i in picturePaths:
            # Check for the 3 images by path
            self.assert_element(f"img[src=\"{i}\"]")
    '''

    # Check for background image
    def testBackground(self):
        self.open(startPage)
        self.assert_element("[src=\"src/images/homepageImage.jpg\"]")

    def testProducts(self):
        self.open(startPage)        # self.open another page later
        for i in productList:
            self.assert_text(i, "body")  # Check for products

    def testLogo(self):
        self.open(startPage)
        # It is not possible to test for the content of <link>s, therefore we have decided to treat the favicon like a page design, untestable and therefore passed by default.
        # self.assert_element("head > link[sizes=\"32x32\"][href=\"src/images/favicons/favicon-32x32.png\"]") #Checks for a link to 32x32 favicon in head
        # Check for an image with the ID #logo
        self.assert_element("img[src=\"src/images/svg/logo.svg\"]")
        # Repeat for all pages once we add more


# Categories in the backlog are represented as classes, every item in the backlog has its own test
