import requests
session = requests.session()
url = 'https://www.yaozh.com/login'
data = {
    'username':'17150522459',
    'pwd':'timf9bhz',
    'formhash':'33B61CD654',
    'backurl':'https%3A%2F%2Fwww.yaozh.com%2F',
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

with session as s:
    s.post(url,data=data,headers=headers)
    res = s.get('https://www.yaozh.com/',headers=headers)
    with open('a.html','w',encoding='utf-8') as f:
        f.write(res.text)