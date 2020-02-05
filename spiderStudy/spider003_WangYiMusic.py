import requests
from lxml import  etree
url = 'https://music.163.com/'
# url = 'https://music.163.com/weapi/copyright/pay_fee_message/config?csrf_token='
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}
# data = {
#     'params':' 0ipnKVzlp9E7vVcUoO1Kushj/QUorjSAFyTFlKtqlFrnl2/P+ekgaYVYvI6q91Iv',
#     'encSecKey': '39e2039f99523c95b67ae610ff35a014b753d5016e83b9be216fc3c2086ccfbaa068e736b19f4d99af7d30a871e3966f91a57fbc336c099e491767f3f8ecf8665b156ed3fed07c9c0d3f93620bfe86f6003185235c55f010545240d406bf88d9013ca75588a0b7859b30f3dbf63cd41f322b1b91436bcd4473eb00fa8b218838',
# }
# response = requests.post(url,data = data)
# print(response.json())
response = requests.get(url,headers=headers).text
s = etree.HTML(response)
file =s.xpath('')
print(file)
