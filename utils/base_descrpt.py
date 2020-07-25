import hashlib
import base64


def _md5(value):
    # 创建md5对象
    hl = hashlib.md5()

    hl.update(value.encode(encoding='utf-8'))
    return hl.hexdigest()


def base64decode(value):
    return base64.b64encode(value.encode('utf8')).decode('utf8')


class Test(object):
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super(Test, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print('__iniT__')



if __name__ == '__main__':
    Test()
