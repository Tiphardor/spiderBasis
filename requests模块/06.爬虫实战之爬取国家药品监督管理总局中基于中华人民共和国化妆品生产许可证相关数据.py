import requests
import json
from fake_useragent import UserAgent

if __name__ == '__main__':
    ua = UserAgent().random
    headers = {'User-Agent': ua}
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    for page in range(1, 3):
        datas = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_text = requests.post(url=url, data=datas, headers=headers).json()
        all_id_list = []
        for data_dict in json_text['list']:
            id = data_dict['ID']
            all_id_list.append(id)

        detail_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
        for id in all_id_list:
            port_datas = {
                'id': id
            }
            response = requests.post(url=detail_url, data=port_datas, headers=headers)
            if response.headers.get('Content-Type') == 'application/json;charset=UTF-8':
                json_text = response.json()
                print(json_text['businessPerson'])

