import json

from zhiyiLianDanLu.multiApi.userInfo import UserInfo


class GetEnvToken():
    def getToken(self):
        self.r = UserInfo().login().text
        self.r_json = json.loads(self.r,strict=False)
        self.token = self.r_json["result"]['token']
        return self.token

