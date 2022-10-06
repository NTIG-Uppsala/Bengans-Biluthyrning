versions = {
    "namn": ["dev/indexDEV.html","index.html", "EN/index.html"]
}

def makeWebsite():
    data = open(versions["namn"][0], 'r', encoding='utf-8')
    f_sv = open(versions["namn"][1], 'w', encoding='utf-8')
    f_en = open(versions["namn"][2], 'w', encoding='utf-8')

    for line in data:
        if 'lang="sv"' in str(line):
            f_sv.write(str(line).replace('<span lang="sv"></span>', ''))
        elif 'lang="en"' in str(line):
            f_en.write(str(line).replace('<span lang="en"></span>', ''))
        else:
            f_sv.write(str(line))
            f_en.write(str(line))
makeWebsite()
