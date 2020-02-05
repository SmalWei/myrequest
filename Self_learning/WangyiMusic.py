import requests
import json
# url = 'https://music.163.com/weapi/v1/resource/comments/A_PL_0_3138801923?csrf_token='
# formdata ={
#     'params': 'caT4bQeYOCN+9RFJmWPMo6igCnaO+FrSqtXscCXuQQ/QsJtfXkNrVtCJOdDC6nr7YZWwcLUM+jD/Ma2ZwcfD7blXbRzMcjIHDNF6SSFhC/UB6u5TV8U0oTGORHy+QpYcGZSgLibHC17kDNICgt4nrKgxcNxov8mVX0wcxmWIsE8k5nnMs18IGM+veDJdRSL9',
#     'encSecKey': '38964abca012d300312b860a4e40e19b84b4a72b9fc47605e461e9e57df2b1c447e6ba08fe26f851db9b821da86311c878a44afe3132db78bb0b1121c08c9a632d322b387ef01dfc1d994d25cc5f0fd5b4144d11a1af30829310ec9a424277fb671327fde041bb64cfefb9e7a2751def972484e0c414894d82bd7914745cd2df'
# }
# headers ={
#     'referer':'https://music.163.com/playlist?id=3138801923',
#     'sec-fetch-mode':'cors',
#     'sec-fetch-site':'same-origin',
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
#
# }
# res = requests.post(url,data=formdata,headers=headers)
# with open('WangyiMusic.json','w',encoding='utf-8') as f:
#     f.write(res.text)
# with open('WangyiMusic.json','r',encoding='utf-8') as f:
#     data = json.load(f)
#     hotComments=data.get("hotComments")
#     for hotComment in hotComments:
#         content = hotComment.get('content')
#         print(content)
#     comments = data.get('comments')
#     print('*'*50)
#     for comment in comments:
#         content = comment.get('content')
#         print(content)
