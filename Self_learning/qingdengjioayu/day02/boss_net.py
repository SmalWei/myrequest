#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@爬虫的本事: 请求和响应，一切与数据为导向
@File    : boss_net.py
@Time    : 2020/1/12 15:51
@Author  : 岁月静好
@Email   : 13546465002@163.com
@Desc  : #  请更换这个文件的描述信息：作用以及目的
"""
# import requests
# import parsel
# url = 'https://www.zhipin.com/c101010100/?'
# def get_parems(page):
#     params = {
#         'query': 'python',
#         'page': str(page),
#         'ka': '0'
#     }
#     return params
# headers  = {
#     'cookie':'_uab_collina=157881626668642280755534; lastCity=101010100; __c=1578815358; sid=sem; toUrl=/; JSESSIONID=""; __g=sem; __l=l=%2Fwww.zhipin.com%2Fbeijing%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D0sKL00c00fDIFkY0luu-0KZEgs741kGX00000DAEgNC00000xs000f.THdBULP1doZA80K85yF9pywd0ZnqmvPbPWDLnW0snj0kPWfdn6Kd5Hf3rDRsrDRdP1wAnHP7nWI7nWKaPRuAP1n4PRfvPYDz0ADqI1YhUyPGujY1nWb1nHmvrHD4FMKzUvwGujYkPBuYUHYkFhcqniuGTZmv5HcYnj6lrjw-nHGWrHGhmhmYrhmkrHmln1F9PWGbrAm1rWPBnhm0uHdCIZwsT1CEQLILIz4lpA-spy38mvqVQ1q1pyfqTvNVgLKlgvFbTAPxuA71ULNxIA-YUAR0mLFW5HDYP1m3%26tpl%3Dtpl_11534_21264_16032%26l%3D1516089153%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26oq%3D%2525E6%25258B%252589%2525E9%252592%2525A9%2525E7%2525BD%252591%26rqlang%3Dcn%26inputT%3D4902&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3DNew-%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-05%26unit%3D%25E5%2593%2581%25E7%2589%258C%252B%25E8%2581%258C%25E4%25BD%258D-%25E4%25BF%25A1%25E6%2581%25AF%26keyword%3DOCPC_boss%25E7%259B%25B4%25E8%2581%2598%25E6%2580%258E%26bd_vid%3D3247162469353380304&friend_source=0&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1578744079,1578815358,1578816312,1578816325; __a=91234548.1578706605.1578744079.1578815358.77.6.20.6; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1578816390; __zp_stoken__=a01fX4UwxDqWUsJLtHWchrJgh6bIFpNmR2ZwqW4j6D1uo6NyCbV01STj5QwKqrInVVHaSNUK6AxQ5sNTI4V3IwnN%2FiCG6YXErkaeL9hvlyfpc9CJNc3L2TZDfhBTv5w3GV13',
#     'referer':'https://www.zhipin.com/beijing/?sid=sem_pz_bdpc_dasou_title',
#     'sec-fetch-mode':'navigate',
#     'sec-fetch-site':'same-origin',
#     'sec-fetch-user':'?1',
#     'upgrade-insecure-requests':'1',
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
# }
# for i in range(8):
#     res = requests.get(url,headers=headers,params=get_parems(i))
#     print(res.text)
    # sel = parsel.Selector(res.text)
    # name = sel.css('h3.name>a::text')
    # print(name)




