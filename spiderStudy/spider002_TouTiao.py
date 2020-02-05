
import requests,json,time
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
def get_page():
    mytime = round(time.time()*1000)
    keyword = "街拍"
    # url = 'https://www.toutiao.com/search_content/?'
    url = 'https://www.toutiao.com/api/search/content/?'
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Cookie': 'tt_webid=6766219808993494536; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6766219808993494536; csrftoken=d7d8ff35f84fd74a11ca9232ed395760; s_v_web_id=3553fb194be249f674e24567a5974872; __tasessionId=7tld21yh61575428635613',
        'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D'
        #  第一步 加headers，cookies，Referer
    }
    params={
        'offset':'0',
        'format': 'json',
        'keyword': keyword,
        'autoload':'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'aid': '24',
        'app_name':'web_search',
        'en_qc': '1',
        'pd': 'synthesis',
        'timestamp': mytime,
    }
    #requests自带params参数能够补全URL可代替urllib.urlopen()的拼接
    response = requests.get(url,headers=headers,params=params)
    print(response.url)
    try:
        if response.status_code == 200:
            #如果状态码为200（即响应成功）则返回json格式的响应内容
            #在requests中自带json()方法
            return json.loads(response.content.decode())
        else:
            return None
    except RequestException as f:
        return f
def main():
    html = get_page()
    #输出响应内容
    with open("tmp.txt", "w+",encoding='utf-8') as fp:
        print(html)
        # fp.write(json.dumps(html))

if __name__ == '__main__':
    main()
