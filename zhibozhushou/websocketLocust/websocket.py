
import json
import time
import websocketnew
from websocketnew import create_connection
from threading import Thread
import _thread


def on_message(ws,message):
    print(message)

def on_errors(ws,error):

    print(error)

def on_close(ws):
    print("close connection")




def on_open(ws):
        # #修改规格：
        # standard = {"activityGoodsId": 3539, "fieldName": "standard", "value": "245", "action": "EDIT_FIELD", "deptType": "1"}
        # #修改店铺名称
        # shopName ={"activityGoodsId":3539,"fieldName":"shopName","value":"小谷粒 XIAOGULI87871","action":"EDIT_FIELD","deptType":"1"}
        # #修改店铺链接
        # shopLink={{"activityGoodsId":3539,"fieldName":"shopLink","value":"http://shop65626181.taobao.com1","action":"EDIT_FIELD","deptType":"1"}}
        # #修改历史最低价
        # minPric ={"activityGoodsId":3539,"fieldName":"minPrice","value":"499","action":"EDIT_FIELD","deptType":"1"}
        # #修改页面价
        # dailyPrice ={"activityGoodsId":3539,"fieldName":"dailyPrice","value":"100","action":"EDIT_FIELD","deptType":"1"}
        # #修改直播间到手价
        # merchantLivePrice = {"activityGoodsId":3539,"fieldName":"merchantLivePrice","value":"100","action":"EDIT_FIELD","deptType":"1"}
        # #修改直播间库存
        # merchantStock = {"activityGoodsId":3539,"fieldName":"merchantStock","value":"1000","action":"EDIT_FIELD","deptType":"1"}
        # #修改佣金比例
        # commissionRate = {"activityGoodsId":3539,"fieldName":"commissionRate","value":"10","action":"EDIT_FIELD","deptType":"1"}
        # #改变商品顺序
        # changePosition={"action":"CHANGE_SORT","activityId":"726","activityGoodsId":3539,"position":0,"optionType":1,"deptType":"1"}
    def run(*args):
        standard = {"activityGoodsId": 3539, "fieldName": "standard", "value": "电话费多个", "action": "EDIT_FIELD",
                    "deptType": "1"}
        ws.send(json.dumps(standard))
        time.sleep(1)
        ws.close()

    def run2(*args):
        shopName ={"activityGoodsId":3539,"fieldName":"shopName","value":"小谷粒","action":"EDIT_FIELD","deptType":"1"}
        ws.send(json.dumps(shopName))
        time.sleep(1)
        ws.close()
    _thread.start_new_thread(run,())
    _thread.start_new_thread(run2, ())




if __name__ == '__main__':
    websocketnew.enableTrace(True)
    # SERVER_URL = 'ws://116.62.106.122:5111/'
    SERVER_URL = 'ws://116.62.106.122:5111/?sid=726missionGoodsDetail&token=99457027-becf-4ac6-ac3e-c5ad2df7bddc'
    #socket保持长连接，一直连接着，就可以使用run_forever方法：
    ws = websocketnew.WebSocketApp(SERVER_URL,
                                   on_message=on_message,
                                   on_error=on_errors,
                                   on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

    # 如果想要通信一条短消息，并在完成后立即断开连接，我们可以使用短连接：
    # ws = create_connection(SERVER_URL)
    # print('修改页面价')
    # ws.send('{"activityGoodsId":3539,"fieldName":"minPrice","value":"299","action":"EDIT_FIELD","deptType":"1"}')
    # print("Sent")
    # print("Receiving")
    # result = ws.recv()
    # print("Received '%s'" %result)
    # ws.close()
