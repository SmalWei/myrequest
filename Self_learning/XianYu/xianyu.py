import execjs
import requests
import time

def get_js_function(js_path, func_name, func_args):
    '''
    获取指定目录下的js代码, 并且指定js代码中函数的名字以及函数的参数。
    :param js_path: js代码的位置
    :param func_name: js代码中函数的名字
    :param func_args: js代码中函数的参数
    :return: 返回调用js函数的结果
    '''

    with open(js_path, encoding='utf-8') as fp:
        js = fp.read()
        ctx = execjs.compile(js)
        return ctx.call(func_name, func_args)


def xianyu():
    url = 'https://h5api.m.taobao.com/h5/mtop.taobao.idle.mach.item.service.faas.item/1.0/?'
    t = time.time()*1000
    sign = get_js_function('xianyu.js', 'yuu',1578215076451)
    print(sign)
    data  = '{"utdid":"e7ee65617aebd","dataSourceId":"376","pageNumber":2,"catIds":""}'
    params = {
        'jsv': '2.5.6',
        'appKey': '12574478',
        't': '1578215076451',
        'sign': '9172084cd68a2eb5de9f307158bc84a4',
        'api': 'mtop.taobao.idle.mach.item.service.faas.item',
        'v': '1.0',
        'uttid': 'e7ee65617aebd',
        'type': 'jsonp',
        'dataType': 'jsonp',
        'callback': 'mtopjsonp3',
        'data': '{"utdid":"e7ee65617aebd","dataSourceId":"376","pageNumber":2,"catIds":""}',
    }
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'thw=cn; t=3cca68e18168b906fd2ecd80e9f19a12; cna=qkmQFovXdEICAXPu8abjrDK5; miid=288752082092749610; cookie2=1bf2bb8c7b32dd9f82b052f0be2b5b07; v=0; _tb_token_=e7ee65617aebd; _m_h5_tk=961f86a2a0324d38bb8d14f8c23af9fd_1578217443291; _m_h5_tk_enc=0a173e31a9df91d23a327566c59b35c8; l=dBMwP0luQjuTgoNfBOfZnurza77tZIRb8sPzaNbMiICP9TCpRrnlWZDfrcT9CnGVnsGpR3PBVv73BoT97yI2bya1-09q3Ipr3dTh.; isg=BCoqgIMuAPR2K4yAE4q3ASDse5DMm671kLffBbTjE31H58uhnClgBWxRd1PeFyaN',
    'referer': 'https://2.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    response = requests.get(url, params=params, headers=headers)

    return response.text

if __name__ == '__main__':

    result = xianyu()
    print(result)
