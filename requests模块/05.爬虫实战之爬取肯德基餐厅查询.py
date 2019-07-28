import requests
import json


if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/75.0.3770.142 Safari/537.36'
    }
    datas = {
        'cname': '厦门',
        'pid': '',
        'keyword': '厦禾路',
        'pageIndex': '1',
        'pageSize': '10'
    }

    response = requests.post(url=url, data=datas, headers=headers)
    list_data = response.json()
    with open('./肯德基位置.json', 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp, ensure_ascii=False)
    print('爬取成功啦！！！')