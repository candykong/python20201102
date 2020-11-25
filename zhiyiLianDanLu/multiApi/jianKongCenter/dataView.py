from zhiyiLianDanLu.baseApi import BaseApi
import json
import yaml

#api = api.Api()
from zhiyiLianDanLu.common.getEnvToken import GetEnvToken


class DataView(BaseApi,GetEnvToken):
    def __init__(self):
        self.token=self.getToken()


    def v2_streamer_collect_list(self):
        #self.data=yaml.safe_load(open("./apiYaml/v2_streamer_collect-list.yaml"))
        #r = api.send(self.data)

        #使用继承和yaml变量替换的方式
        self.data=self.template("./apiYaml/v2_streamer_collect-list.yaml",{"gray_df_token":self.token})
        r=self.send(self.data)
        print(r.text)
        return r
