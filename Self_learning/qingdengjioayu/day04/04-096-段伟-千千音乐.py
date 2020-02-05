# """
#     目标网址：http://music.taihe.com/artist/2517
#
#     前排提示：parsel.Selector 能将html代码自动补全
#
#     爬取薛之谦的前三个页面下的所有歌曲，保存到当前文件夹下
#
#     将`歌名`、`专辑名`、`时长`写入excel表格，表名为`薛之谦`，文件命名为`薛之谦.xlsx`
#
#     选做：将文件在磁盘中的路径也保存到`薛之谦`表中的`文件路径`字段
# """
import requests
import parsel
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
# }
# urls = [f'http://music.taihe.com/data/user/getsongs?start={start}&size=15&ting_uid=2517&.r=0.77607506252396591578733372118' for start in range(0,150,15)]
# for url in urls:
#     res  = requests.get(url,headers=headers)
#     data = res.json()['data']['html'].strip()
#     sel = parsel.Selector(data)
#     lis = sel.xpath("//ul/li[@class=' songlist-item  bb-dotimg clearfix   song-item-hook   csong-item-hook   ']")
#     for li in lis:
#         songname = li.xpath("./div/span[@class='songname']/a/@title").get()
#         album = li.xpath("./div[3]/a/@title").get()
#         songtime = li.xpath("./div[@class='songlist-inline songlist-time']/text()").get().strip()
#         print(songname,album,songtime)

