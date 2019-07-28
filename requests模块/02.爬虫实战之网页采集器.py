import requests

if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    kw = input('please enter a word:')
    param = {
        'query': kw
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    file_name = kw + '.html'
    with open(file_name, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(file_name, "保存数据成功！！！")
