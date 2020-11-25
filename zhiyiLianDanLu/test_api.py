from unittest import TestCase
from zhiyiLianDanLu.baseApi import Api



class TestApi(TestCase):
    data = {
        "method": "get",
        "url": "/security-api/v2/user-info",
        "headers":{
            "token": "e72103c5-41ef-4fba-ab37-5fee26beb908"
        }
    }

    def test_send(self):
        api=Api()
        r=api.send(self.data)
        print(r.text)
