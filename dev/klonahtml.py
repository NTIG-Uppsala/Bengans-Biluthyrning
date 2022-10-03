versions = {
    "dev/indexDEV.html": ["index.html", "EN/index.html"],
    "dev/productsDEV.html": ["produkter.html", "EN/products.html"],
    "dev/staffDEV.html": ["personal.html", "EN/staff.html"]
}

cards = {
    "audiA6": ["audiA6.jpg", "Audi A6", "800"], 
    "renaultKadjar": [None, "Renault Kadjar", "450"],
    "kiaSoul": [None, "Kia Soul", "400"],
    "subaruOutback": ["subaruOutback.jpg", "Subaru Outback", "300"],
    "cadillacEscalade": ["cadillacEscalade.jpg", "Cadillac Escalade", "500"],
    "mitsubishiOutlander": ["mitsubishiOutlander.jpg", "Mitsubishi Outlander", "450"],
    "volvoXC40": ["volvoXC40.jpg", "Volvo XC40", "800"],
    "vwPolo": ["vwPolo.jpg", "VW Polo", "300"],
    "kiaCarens": [None, "Kia Carens", "500"]
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
            if '<!--Cards go here-->' in str(line):
                for j in cards:
                    card = str(line).split("<!--Cards go here-->")[0]+'<div class="productsMainFlexCard" id="{}">\n'.format(j)
                    card += str(line).split("<!--Cards go here-->")[0]+'<div class="cardImage">\n'
                    if cards [j][0] != None:
                        card += str(line).split("<!--Cards go here-->")[0]+'\t<img src="src/images/products/{}">\n'.format(cards[j][0])
                    card += str(line).split("<!--Cards go here-->")[0]+'</div>\n'
                    f_sv.write(card+str(line).split("<!--Cards go here-->")[0]+"</div>\n")

makeWebsite()