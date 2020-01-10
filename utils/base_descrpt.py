import hashlib
import base64


def _md5(value):
    # 创建md5对象
    hl = hashlib.md5()

    hl.update(value.encode(encoding='utf-8'))
    return hl.hexdigest()


def base64decode(value):
    return base64.b64encode(value.encode('utf8')).decode('utf8')


if __name__ == '__main__':
    print(_md5('112'))
    print(base64decode('abcd'),type(base64decode('abcd')))




