"""
    请求拉勾网 python 前十页的招聘数据，并将信息写入到一个txt文本里面。
    (温馨提示：速度不要太快，小心被封)

    需求1：获取一下信息
        'city': 城市
        'companyFullName': 公司名
        'companySize': 公司规模
        'education': 学历
        'positionName': 职位名称
        'salary': 薪资
        'workYear': 工作时间

    需求2：以逗号（,）分割信息内容，写入文件。要求文件名为 `拉钩职位信息.csv`。
    例如：
        上海,上海沸橙信息科技有限公司,150-500人,本科,python,8k-12k,不限

作业提交格式
    + 使用源代码的方式提交，题目用 `注释` 的方式写在源代码里面。
    + 作业文件命名：第几次作业-编号-作业编号-姓名.py（例如02-00-01-正心.py）
    + 提交到QQ邮箱：2328074219@qq.com
"""
import requests

# with requests.session() as s:
#
#     s.cookies.clear()
#     cookie_url ='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
#     s.post(cookie_url,data=cookies_data)
#
#     res = s.get(url,headers=headers,data=data)
#     print(res.text)
# cookies_url ='https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# cookies_headers ={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
# }
# for i in range(1,8):
#     with requests.session() as s:
#         s.cookies.clear()
#         s.get(cookies_url, headers=cookies_headers)
#         url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
#         headers = {
#             'Host': 'www.lagou.com',
#             'Origin': 'https://www.lagou.com',
#             'Referer': 'https://www.lagou.com/jobs/list_python/p-city_0?px=default',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4020.0 Safari/537.36',
#             'X-Requested-With': 'XMLHttpRequest',
#         }
#         data = {
#             'first': 'true',
#             'pn': str(i),
#             'kd': 'python',
#         }
#         res = s.get(url, headers=headers, data=data)
#         result = res.json()['content']['positionResult']['result']
#         print(len(result),result)

def get_cookie():
    """
    每一次请求之前都去获取新的cookies
    cookie一般都是服务器生成
    获取cookie
    """
    cookie = requests.get("https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=", headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'},
                          allow_redirects=False).cookies
    # 默认情况下 会重定向到登录页面
    return cookie


# 接口api
url = 'https://www.lagou.com/jobs/positionAjax.json'
headers = {
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}
params = {
    'needAddtionalResult': 'false'
}


def get_data(flag, page, sid):
    """
    使用函数 可以多次调用表
    用一个方法
    专门构建请求参数
    """
    data = {
        'first': flag,
        'pn': page,
        'kd': 'python',
        'sid': sid
    }
    return data


# 从拿一页开始
page = 1
sid = ""

# 用for循环构建翻页爬取
for i in range(20):
    # time.sleep(5)
    # flag 第一页是 true 从第二页开始时false
    if page == 1:
        flag = True
    else:
        flag = False
    response = requests.post(url=url, headers=headers, params=params, data=get_data(flag, page, sid),
                             cookies=get_cookie())

    # print(response.text)
    sid = response.json()['content']['showId']
    text = response.json()['content']['positionResult']['result']
    # 打开的是普通文件 windows 默认使用 gbk utf-8
    with open("result.csv", "a", encoding='utf_8_sig') as file:
        for cp in text:
            cp_msg = f"{cp['city']},{cp['companyFullName']},{cp['companySize']},{cp['education']},{cp['positionName']},{cp['salary']},{cp['workYear']}\n"
            file.write(cp_msg)
    print(f"第{page}页爬取完成")
    page += 1

print("爬取完成")

# 需求1将csv后缀改成TXT即可，可能需要encoding

