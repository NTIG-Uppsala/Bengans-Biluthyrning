from seleniumbase import BaseCase  # importing testing framework
import pathlib
import re

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "EN/index.html"  # Path to index.html

productPage = filePath + "EN/products.html"  # Path to products.html

employeePage = filePath + "EN/staff.html" # Path to employees.html

pages = [startPage, productPage, employeePage]


socialLinks = ["https://sv-se.facebook.com/ntiuppsala/", "https://twitter.com/ntiuppsala/",
               "https://www.instagram.com/ntiuppsala/"]  # Relevant social media links
socialMediaPaths = ["../src/images/svg/facebookIcon.svg", "../src/images/svg/twitterIcon.svg",
                    "../src/images/svg/instagramIcon.svg"]  # Paths for different social media .svg imgs

# This is more accepting, but less human-readable and therefore not currently used
# openHours = ["Vardagar[\\s:]+10[:.]?0{0, 2} ?- ?16[:.]?0{0, 2}",
# "Lördagar[\\s:]+12[:.]?0{0, 2} ?- ?15[:.]?0{0, 2}",
# "Söndagar[\\s:]+Stängt"]

openHours = {
    "Weekdays:": "10-16",
    "Saturdays:": "12-15",
    "Sundays:": "Closed"
}

contactInfo = ["Fjällgatan 32H,?\\s+981 39\\s+Jönköping",
               "0630-555[- ]555", "info.bengans@gmail.com"]


class footer(BaseCase):
    def testSocials(self):
        # Finds social media icons in every footer
        for i in pages:
            for j in range(len(socialMediaPaths)):
                self.open(i)
                # Check that the icon link exists, and clicks if it does
                self.click(f"[src=\"{socialMediaPaths[j]}\"]")
                # Checks that links lead to the right place
                if (self.get_current_url() != socialLinks[j]):
                    raise NameError(f"Failed at {socialMediaPaths[j]} in {i}")

    def testOpenHours(self):
        # Finds open hour in every footer
        for i in pages:
            self.open(i)
            footerText = self.get_text(".footer")
            # Matches footer text to regex regarding open hours
            for j in openHours:
                x = re.compile(f"{j}\\s+{openHours[j]}")
                if not x.search(footerText):
                    # Raises an error if correct text is not found
                    raise NameError(f"{j[:-1]} not correct")

    def testContactInfo(self):
        # Finds contact info in every footer
        for i in pages:
            self.open(i)
            footerText = self.get_text(".footer")
            # Matches footer text to regex contact info
            for j in contactInfo:
                x = re.compile(j)
                if not x.search(footerText):
                    # Raises an error if correct text is not found
                    raise NameError(f"{j} does not match found text.")

    def testLinks(self):
        for i in pages:
            self.open(i)

            self.assert_element('.contact[href=\"tel:0630555555\"]')
            self.assert_element('.contact[href=\"mailto:info.bengans@gmail.com\"]')