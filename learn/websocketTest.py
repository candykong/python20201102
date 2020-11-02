#!/usr/bin/python
# -*- coding:UTF-8 -*-'

import websocket
import json
from learn.locust import HttpUser, task,between

'''
url = 'ws://116.62.106.122:5111/?sid=522&token=99457027-becf-4ac6-ac3e-c5ad2df7bddc'  #websocket连接地址
ws = websocket.create_connection(url)  #创建连接
#data为json格式
data = {"activityGoodsId":2557,"fieldName":"standard","value":"2","action":"EDIT_FIELD","deptType":"1"}
ws.send(json.dumps(data))   #json转化为字符串，必须转化
print(ws.recv())    #服务器响应数据
ws.close()   #关闭连接
'''



class UpdateZhibo(HttpUser):
    host = "http://dev-live-assistant.zhiyitech.cn"
    wait_time = between(1, 2)
    SERVER_URL = 'ws://116.62.106.122:5111/?sid=522&token=99457027-becf-4ac6-ac3e-c5ad2df7bddc'
    def on_start(self):
        ws = websocket.create_connection(self.SERVER_URL)

    @task(1)
    def test(self):
        send_info = {"activityGoodsId": 2557, "fieldName": "standard", "value": "2", "action": "EDIT_FIELD",
                     "deptType": "1"}
        while (True):
            self.ws.send(json.dumps(send_info))
            while (1):
                response = self.ws.recv()
                result = json.loads(response)['msg']
                if result == 'SUCCESS':
                    print('修改成功')
                else:
                    print('修改失败')



