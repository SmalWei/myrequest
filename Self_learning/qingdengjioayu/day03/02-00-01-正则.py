"""
    使用python请求此页面：https://www.pearvideo.com/video_1639869 将在获取的文本中会有下面这段内容

    var contId="1639869",liveStatusUrl="liveStatus.jsp",liveSta="",playSta="1",autoPlay=!1,isLiving=!1,isVrVideo=!1,hdflvUrl="",sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",srcUrl="https://video.pearvideo.com/mp4/adshort/20200107/cont-1639869-14773063_adpkg-ad_hd.mp4",vdoUrl=srcUrl,skinRes="//www.pearvideo.com/domain/skin",videoCDN="//video.pearvideo.com";
var player;

    请将其中的视频连接提取出来，并将视频下载到本地。视频名为页面的标题
"""
import requests
import re
url = 'https://www.pearvideo.com/video_1639869'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
rule =r'srcUrl="(.*?)",v'
res = requests.get(url,headers=headers)
vedio_url  =re.findall(rule,res.text)
res = requests.get(vedio_url[0],headers=headers)
with open('a.mp4','wb') as w:
    w.write(res.content)

