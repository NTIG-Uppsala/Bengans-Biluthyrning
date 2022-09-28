versions = {
    "dev/indexDEV.html": ["index.html", "EN/index.html"],
    "dev/productsDEV.html": ["produkter.html", "EN/products.html"],
    "dev/staffDEV.html": ["personal.html", "EN/staff.html"]
}

def makeWebsite():
    for i in versions:
        data = open(i, 'r', encoding='utf-8')
        f_sv = open(versions[i][0], 'w', encoding='utf-8')
        f_en = open(versions[i][1], 'w', encoding='utf-8')

        for line in data:
            if 'lang="sv"' in str(line):
                f_sv.write(str(line).replace('<span lang="sv"></span>', ''))
            elif 'lang="en"' in str(line):
                f_en.write(str(line).replace('<span lang="en"></span>', ''))
            else:
                f_sv.write(str(line))
                f_en.write(str(line))

makeWebsite()