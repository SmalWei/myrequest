import requests
import time
import execjs
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers ={
    'cookie': 'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=FECAA3D38F0CF92F3FA01E53FE8D490D:FG=1; PSTM=1577671188; BIDUPSID=34EE4B5EA46526DE9F2FF6C42A0C497B; BDUSS=wzU1drMWVucUtoRUFIRFFvQ2ZQVDE4YndmdmJCT2x-WFFTUmllNFI1d2FBREZlSUFBQUFBJCQAAAAAAAAAAAEAAACB-Gdp4LjguLDCsMJ3bwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABpzCV4acwleZE; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; delPer=0; H_PS_PSSID=1469_21090_30210_30489_30283_26350_30501; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1577699083,1577703086,1577709210,1577838974; yjs_js_security_passport=0ccd717f9cf57f99cbae7c11150e2df831eb5e6f_1577838982_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1577839104; __yjsv5_shitong=1.0_7_90cabb9118ad430823a9f29caca35ed50294_300_1577839105256_223.223.183.28_fe09501c',
    'origin': 'https://fanyi.baidu.com',
    'referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=spider%0D%0A%0D%0A&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

def Baidutanslate(query):
    with open('my.js', 'r', encoding='utf-8') as f:
        ctx = f.read()
        func1 = execjs.compile(ctx)
        sign = func1.call('Baidutra',query)
    formdata = {
        'from': 'en',
        'to': 'zh',
        'query': query,
        'simple_means_flag': '3',
        'sign': sign,
        'token': 'b753d1adc574c9bc119d911a7b67d00b',
    }
    res  = requests.post(url,headers=headers,data=formdata)
    print(res.json())
Baidutanslate('apple')