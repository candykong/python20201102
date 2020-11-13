from zhiyiLianDanLu import api
import json
import yaml

api = api.Api()

class DataView():
    def v2_streamer_collect_list(self):
        self.data=yaml.safe_load(open("./apiYaml/v2_streamer_collect-list.yaml"))
        r = api.send(self.data)
        print(r.text)
        return r
