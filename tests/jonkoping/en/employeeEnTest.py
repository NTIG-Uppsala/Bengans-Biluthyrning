from seleniumbase import BaseCase  # importing testing framework
import pathlib

# Find file path and prepare formatting, gets file, removes the last 5 characters
filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-18].replace("\\", "/")

startPage = filePath + "jonkoping/en/index.html"  # Path to index.html

productPage = filePath + "jonkoping/en/products.html"  # Path to products.html

employeePage = filePath + "jonkoping/en/staff.html"  # Path to employees.html

employeeList = [
    ["annaPettersson","anna_pettersson.jpg","Anna Pettersson", "CEO"], 
    ["fredrikOrtqvist","fredrik_ortqvist.jpg", "Fredrik Örtqvist", "Customer support"], 
    ["peterJohansson","peter_johansson.jpg", "Peter Johansson","Customer support"]
]

class workingWebsite(BaseCase):
    def testTitle(self):
        self.open(productPage)
        self.assert_title("Bengan's Car Rentals")

class employees(BaseCase):
    def testNames(self):
        self.open(employeePage)
        for i in employeeList:
            self.assert_text(i[2], "#"+i[0])
            self.assert_text(i[3], "#"+i[0])
            if i[1] != None:
                self.assert_element("#"+i[0]+' .cardImage2 img[src="../../src/images/personal/'+i[1]+'"]')
