# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/8 19:32
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : sem_config.py
# @Software : PyCharm
from influence_token.influence_token import ToKen

token = ToKen()

print(token)

class sem_config:

    def sem_url(self):
        self.url = ''

    def sem_headers(self):

        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Authorization": token,
            "Connection": "keep-alive",
            "Host": "gateway.test.vevor.net",
            "Origin": "http://scp.test.vevor.net",
            "Referer": "http://scp.test.vevor.net/",
            "sec-ch-ua": '"Google Chrome";v="87", "\"Not;A\\Brand";v="99", "Chromium";v="87"',
            "sec-ch-ua-mobile": "?0",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }
        return self.headers
