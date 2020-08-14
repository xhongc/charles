import time

from django.conf import settings
from qiniu import Auth, put_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class HomePageCut(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('window-size=1366x768')  # 指定浏览器分辨率
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors",
                                                                   "enable-automation"])
        chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

        self.driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/local/bin/chromedriver')

    def cut(self, url, out):
        try:
            self.driver.get(url)
            self.driver.save_screenshot(out)
            return True
        except:
            return False
        finally:
            time.sleep(1)
            self.driver.quit()


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }


def upload_qiniu(key, uid):
    access_key = settings.QINIU_ACCESS_KEY
    secret_key = settings.QINNIU_SECRET_KEY

    q = Auth(access_key, secret_key)

    bucket_name = settings.BUCKET_NAME


    # 上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
    policy = {
        'callbackUrl': settings.QINNIU_CALLBACK_URL,
        'callbackBody': 'filename=$(fname)&filesize=$(fsize)&uid=%s' % uid
    }

    token = q.upload_token(bucket_name, key, 3600, policy)

    localfile = './out.png'

    ret, info = put_file(token, key, localfile)
    print(info)
