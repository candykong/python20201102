import yaml

from zhiyiLianDanLu.baseApi import BaseApi


class UserInfo(BaseApi):
    def login(self):
        self.data=yaml.safe_load(open("./apiYaml/phone-code-login.yaml"))
        r =self.send(self.data)
        return r