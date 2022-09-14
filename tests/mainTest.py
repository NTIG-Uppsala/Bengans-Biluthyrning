from seleniumbase import BaseCase  # importing testing framework
import pathlib

# To start the test, run "python -m pytest .\mainTest.py" in "\Bengans-Biluthyrning\tests"
# or "python -m pytest .\tests\mainTest.py" in "\Bengans-Biluthyrning"

# Find file path and prepare formatting
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

productPage = filePath + "products.html"  # Path to products.html

socialLinks = ["https://sv-se.facebook.com/ntiuppsala/", "https://twitter.com/ntiuppsala",
               "https://www.instagram.com/ntiuppsala/"]  # Relevant social media links
socialMediaPaths = ["src/images/svg/facebookIcon.svg", "src/images/svg/twitterIcon.svg",
                    "src/images/svg/instagramIcon.svg"]  # Paths for different social media .svg imgs

class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(startPage)
        self.assert_title("Bengans Biluthyrning")
    
    def testName(self):
        self.open(startPage)
        self.assert_text("Bengans Biluthyrning")
    
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
        footerText = self.get_text("#footer")
        




# Categories in the backlog are represented as classes, every item in the backlog has its own test
