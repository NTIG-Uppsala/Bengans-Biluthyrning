from seleniumbase import BaseCase  # importing testing framework
import pathlib
import re

# To start the test, run "python -m pytest .\productTest.py" in "\Bengans-Biluthyrning\tests"
# or "python -m pytest .\tests\productTest.py" in "\Bengans-Biluthyrning"

# Find file path and prepare formatting
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

productPage = filePath + "products.html"  # Path to products.html

socialLinks = ["https://sv-se.facebook.com/ntiuppsala/", "https://twitter.com/ntiuppsala/",
               "https://www.instagram.com/ntiuppsala/"]  # Relevant social media links
socialMediaPaths = ["src/images/svg/facebookIcon.svg", "src/images/svg/twitterIcon.svg",
                    "src/images/svg/instagramIcon.svg"]  # Paths for different social media .svg imgs

# Make these more flexible
openHours = {
    "Vardagar:": "10-16",
    "Lördagar:": "12-15",
    "Söndagar:": "Stängt"
}

contactInfo = ["Fjällgatan 32H,\\s+981 39 Jönköping",
               "0630-555[- ]555", "info.bengans@gmail.com"]

productlist = [
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
        self.assert_title("Bengans Biluthyrning")

class footer(BaseCase):
    def testSocials(self):
        for i in range(len(socialMediaPaths)):
            self.open(productPage)
            # Check that the icon link exists, and clicks if it does
            self.click(f"[src=\"{socialMediaPaths[i]}\"]")
            # Checks that links lead to the right place
            if (self.get_current_url() != socialLinks[i]):
                raise NameError(f"Failed at {socialMediaPaths[i]}")

    def testOpenHours(self):
        self.open(productPage)
        footerText = self.get_text(".footer")
        for i in openHours:
            x = re.compile(f"{i}\\s+{openHours[i]}")
            if not x.search(footerText):
                raise NameError(f"{i[:-1]} not correct")

    def testContactInfo(self):
        self.open(productPage)
        footerText = self.get_text(".footer")
        for i in contactInfo:
            x = re.compile(i)
            if not x.search(footerText):
                raise NameError(f"{i} does not match found text.")


class header(BaseCase):
    def testName(self):
        self.open(productPage)
        self.assert_text("Bengans Biluthyrning", "#header")

    def testMenu(self):
        self.open(productPage)
        self.assert_element("#header a[href=\"index.html\"]")
    
    def testLogo(self):
        self.open(productPage)
        #self.assert_element(
        #    "#header > a[\"href=index.html\"] > [src=\"src/images/svg/logo.svg\"]")
        self.assert_element("#header [src=\"src/images/svg/logo.svg\"]")
    
class products(BaseCase):
    def testProducts(self):
        self.open(productPage)
        for i in productlist:
            self.assert_text(i)




# Categories in the backlog are represented as classes, every item in the backlog has its own test
