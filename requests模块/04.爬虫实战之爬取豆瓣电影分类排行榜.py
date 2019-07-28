import requests
import json


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/75.0.3770.142 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/chart/top_list?'
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    response = requests.get(url=url, params=params, headers=headers)
    list_data = response.json()
    with open('./豆瓣.json', 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp, ensure_ascii=False)
    print('爬取成功！！！')