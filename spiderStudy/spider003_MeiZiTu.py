import requests
from lxml import etree

i = 0
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3088.3 Safari/537.36","Referer":"http://www.mzitu.com/all/"}
url = 'https://www.mzitu.com/tag/meitun/page/2/'		# 此处网址根据需要修改
data = requests.get(url,headers=headers).text
s = etree.HTML(data)
file = s.xpath('//*[@id="pins"]/li')

for div in file:
    url_te = div.xpath('./a/@href')[0]
    data_te = requests.get(url_te,headers=headers).text
    s_te = etree.HTML(data_te)
    page = int(s_te.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')[0])

    # 图片列表页
    for x in range(1,page):
        urls = url_te + '/' + str(x)
        data_s = requests.get(urls,headers=headers).text
        s_s = etree.HTML(data_s)
        img_url = s_s.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')[0]
        r = requests.get(img_url,headers=headers)
        # 保存图片
        path  = "image" + "\\"+ str(i) +'.png'	# 此处路径需要修改
        with open(path,'wb') as f:
            f.write(r.content)
        i+=1