import requests
import json


if __name__ == '__main__':
    word = input('please enter a word:')
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    data = {
        'kw': word
    }
    response = requests.post(url=url, data=data, headers=headers)
    json_data = response.json()
    file_name = word + '.json'
    with open(file_name, 'w', encoding='utf-8') as fp:
        json.dump(json_data, fp, ensure_ascii=False)
    print('爬虫成功！！！')