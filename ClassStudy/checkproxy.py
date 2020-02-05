import requests
proxies = {
  "http": "36.25.243.51:80",
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
response = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)
print(response.status_code)

