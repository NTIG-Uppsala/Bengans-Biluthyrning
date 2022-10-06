versions = {
    "dev/indexDEV.html": ["sv/index.html", "en/index.html"],
    "dev/productsDEV.html": ["sv/produkter.html", "en/products.html"],
    "dev/staffDEV.html": ["sv/personal.html", "en/staff.html"]
}

# cards = {
#     "audiA6": ["audiA6.jpg", "Audi A6", "Automat", "Automatic", "800", "PLACEHOLDER"], 
#     "renaultKadjar": [None, "Renault Kadjar", "Automat", "Automatic", "450", "PLACEHOLDER"],
#     "kiaSoul": [None, "Kia Soul", "Manuell", "Manual", "400", "PLACEHOLDER"],
#     "subaruOutback": ["subaruOutback.jpg", "Subaru Outback", "Manuell", "Manual", "300", "PLACEHOLDER"],
#     "cadillacEscalade": ["cadillacEscalade.jpg", "Cadillac Escalade", "Manuell", "Manual", "500", "PLACEHOLDER"],
#     "mitsubishiOutlander": ["mitsubishiOutlander.jpg", "Mitsubishi Outlander", "Manuell", "Manual", "450", "PLACEHOLDER"],
#     "volvoXC40": ["volvoXC40.jpg", "Volvo XC40", "Automat", "Automatic", "800", "PLACEHOLDER"],
#     "vwPolo": ["vwPolo.jpg", "VW Polo", "Manuell", "Manual", "300", "PLACEHOLDER"],
#     "kiaCarens": [None, "Kia Carens", "Manuell", "Manual", "500", "PLACEHOLDER"]
# }

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
            # if '<!--Cards go here-->' in str(line):
            #     for j in cards:
            #         cardStart = str(line).split("<!--Cards go here-->")[0]+'<div class="productsMainFlexCard" id="{}">\n'.format(j)
            #         cardStart += str(line).split("<!--Cards go here-->")[0]+'<div class="cardImage">\n'
            #         cardSV = ""
            #         cardEN = ""
            #         if cards [j][0] != None:
            #             cardSV += str(line).split("<!--Cards go here-->")[0]+'\t<img src="src/images/products/{}">\n'.format(cards[j][0])
            #             cardEN += str(line).split("<!--Cards go here-->")[0]+'\t<img src="src/images/products/{}">\n'.format(cards[j][0])
            #         cardStart += str(line).split("<!--Cards go here-->")[0]+'</div>\n'
            #         cardStart += str(line).split("<!--Cards go here-->")[0]+'<div class="cardText">\n<h1>{}</h1>\n'.format(cards[j][1])
            #         cardSV += str(line).split("<!--Cards go here-->")[0]+'<p>{}</p>'.format(cards[j][2])
            #         cardEN += str(line).split("<!--Cards go here-->")[0]+'<p>{}</p>'.format(cards[j][3])
            #         cardEnd = str(line).split("<!--Cards go here-->")[0]+'</div>\n'                   
            #         cardEnd += str(line).split("<!--Cards go here-->")[0]+"</div>\n"
            #         f_sv.write(cardStart + cardSV + cardEnd)
            #         f_en.write(cardStart + cardEN + cardEnd)

makeWebsite()