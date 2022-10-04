from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

startPage = filePath + "index.html"  # Path to index.html

productPage = filePath + "produkter.html"  # Path to products.html

employeePage = filePath + "personal.html"  # Path to employees.html

employeeList = [
    ["AnnaPettersson","anna_pettersson.jpg","Anna Pettersson", "VD"], 
    ["FredrikOrtqvist","fredrik_ortqvist.jpg", "Fredrik Örtqvist", "Kundservice"], 
    ["PeterJohansson","peter_johansson.jpg", "Peter Johansson","Kundservice"]
]

class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(productPage)
        self.assert_title("Bengans Biluthyrning")

class employees(BaseCase):
    def testNames(self):
        self.open(employeePage)
        for i in employeeList:
            self.assert_text(i[2], "#"+i[0])
            self.assert_text(i[3], "#"+i[0])
            self.assert_text(i[4], "#"+i[0])
            if i[1] != None:
                self.assert_element("#"+i[0]+' .cardImage img[src="src/images/personal/'+i[1]+'"]')
