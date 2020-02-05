from fontTools.ttLib import TTFont


font =  TTFont("cateye.woff")
# font.saveXML('cateye.xml')
Cmap = font.getBestCmap()
font_dict = {}
for index,value in Cmap.items():
    font_dict[hex(int(index))] = value



