import requests
import json

T_content = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": ""
        },
        "inputImage": {
            "url": ""
        },
        "selfInfo": {
            "location": {
                "city": "福州",
                "province": "福建省",
                "street": "台江"
            }
        }
    },
    "userInfo": {
        "apiKey": "0fc11f3ac8bd4f74ba88125e526874e4",
        "userId": "wechat"
    }
}


def tuling(content):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    data = T_content
    data['perception']['inputText']['text'] = content
    resp = requests.post(url, data=json.dumps(data))
    print(resp.text)


def sizhi(content):
    url = 'https://api.ownthink.com/bot'
    data = {
        "spoken": content,
        "appid": "xiaosi",
        "userid": "charles"
    }
    try:
        resp = requests.post(url, data=data)
        resp = json.loads(resp.text)
        if resp.get('message', '') == 'success':
            return resp.get('data').get('info').get('text')
        else:
            return '你说啥呢？'
    except Exception as e:
        print(e)
        return '咱也不知道'


if __name__ == '__main__':
    a = sizhi('在哪呢')
    print(a)
