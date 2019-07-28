import requests
from fake_useragent import FakeUserAgent
from bs4 import BeautifulSoup

headers = {'User-Agent': FakeUserAgent().random}


def parse_content(url):
    page_text = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    content = soup.select('.chapter_content')[0].text
    return content


if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    a_elements = soup.select('.book-mulu > ul > li > a')
    chapter = 1
    for a_ele in a_elements:
        print('开始下载第%d章节' % chapter)
        title = a_ele.text
        content_url = 'http://www.shicimingju.com' + a_ele['href']
        content = parse_content(content_url)

        with open('./sanguo.txt', 'a+', encoding='utf-8') as fp:
            fp.write(title + ":" + content + '\n\n\n\n\n')
            print('第%d章节下载完毕！！！' % chapter)
        chapter += 1