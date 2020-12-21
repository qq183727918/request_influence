# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/9 17:30
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : influence_token.py
# @Software : PyCharm
import requests
from params.sem_params import ParamsTest
from time import sleep


class SemLoginTest:
    def semtoken(self):
        querystring = {"username": "13925731395", "password": "c90a3167151be42f910045215f6aac96",
                       "grant_type": "password"}

        url = "https://gatewaypre.vevor.net/center-user-service/controller-authLoginController/login?username=13925731395&password=c90a3167151be42f910045215f6aac96&grant_type=password"

        payload = ""

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic YXV0aDoxMjM="
        }

        response = requests.post(url, data=payload, headers=headers, params=querystring)

        re = response.json()

        import pprint
        pprint.pprint(re)


if __name__ == '__main__':
    sem = SemLoginTest()
    sem.semtoken()
