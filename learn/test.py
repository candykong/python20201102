#! /usr/bin/python
# coding=utf-8
import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))
    #data 是一个请求的信息
    def send(self,data:dict):
        url = self.env["dev-live-assistant.zhiyitech.cn"][self.env["default"]]+\
              str(data["url"])
        print(url)
        r = requests.request(method=data["method"] ,url=url,headers=data["headers"],params=data["json"])
        print(r.text)


if __name__ == '__main__':

    data = {
            "method": "get",
            "url": "/security-api/v2/user-info",
            "headers":{
                "token": "e72103c5-41ef-4fba-ab37-5fee26beb908"
            },
            "json":{}
        }
    api=Api()
    api.send(data)