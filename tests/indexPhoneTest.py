from seleniumbase import BaseCase  # importing testing framework
import pathlib
import re

# To start the test, run "python -m pytest .\indexTest.py" in "\Bengans-Biluthyrning\tests"
# or "python -m pytest .\tests\indexTest.py" in "\Bengans-Biluthyrning"

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

productPage = filePath + "products.html"  # Path to products.html

socialLinks = ["https://sv-se.facebook.com/ntiuppsala/", "https://twitter.com/ntiuppsala/",
               "https://www.instagram.com/ntiuppsala/"]  # Relevant social media links
socialMediaPaths = ["src/images/svg/facebookIcon.svg", "src/images/svg/twitterIcon.svg",
                    "src/images/svg/instagramIcon.svg"]  # Paths for different social media .svg imgs

# This is more accepting, but less human-readable and therefore not currently used
# openHours = ["Vardagar[\\s:]+10[:.]?0{0, 2} ?- ?16[:.]?0{0, 2}",
             # "Lördagar[\\s:]+12[:.]?0{0, 2} ?- ?15[:.]?0{0, 2}",
             # "Söndagar[\\s:]+Stängt"]

openHours = {
    "Vardagar:": "10-16",
    "Lördagar:": "12-15",
    "Söndagar:": "Stängt"
}

contactInfo = ["Fjällgatan 32H,\\s+981 39 Jönköping",
               "0630-555[- ]555", "info.bengans@gmail.com"]


class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(startPage)
        self.assert_title("Bengans Biluthyrning")
    
    def testBackground(self):
        self.open(startPage)
        self.assert_element(".backgroundImage")


class footer(BaseCase):
    def testSocials(self):
        for i in range(len(socialMediaPaths)):
            self.open(startPage)
            # Check that the icon link exists, and clicks if it does
            self.click(f"[src=\"{socialMediaPaths[i]}\"]")
            # Checks that links lead to the right place
            if (self.get_current_url() != socialLinks[i]):
                raise NameError(f"Failed at {socialMediaPaths[i]}")

    def testOpenHours(self):
        self.open(startPage)
        footerText = self.get_text(".footer")
        # Matches footer text to regex regarding open hours
        for i in openHours:
            x = re.compile(f"{i}\\s+{openHours[i]}")
            if not x.search(footerText):
                # Raises an error if correct text is not found
                raise NameError(f"{i[:-1]} not correct")

    def testContactInfo(self):
        self.open(startPage)
        footerText = self.get_text(".footer")
        # Matches footer text to regex contact info
        for i in contactInfo:
            x = re.compile(i)
            if not x.search(footerText):
                # Raises an error if correct text is not found
                raise NameError(f"{i} does not match found text.")


class header(BaseCase):
    def testName(self):
        self.open(startPage)
        self.assert_text("Bengans Biluthyrning", "#header")

    def testMenu(self):
        self.open(startPage)
        self.click("label")
        self.assert_element("nav a[href=\"products.html\"]")
        self.assert_element("nav a[href=\"index.html\"]")
        
    def testLogo(self):
        self.open(startPage)
        self.assert_element("#header [src=\"src/images/svg/logo.svg\"]")