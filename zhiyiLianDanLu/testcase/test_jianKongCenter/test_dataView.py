#!/usr/bin/python
# -*- coding:UTF-8 -*-

import pytest
import  pytest_assume
import requests
import json

from zhiyiLianDanLu.multiApi.jianKongCenter.dataView import DataView



class Test_dataView():
    def setup_class(self):
        print("开始测试")

    # @pytest.mark.parametrize("myMonitor",[0,1,2])
    # @pytest.mark.parametrize("rankStatus",[1,2])
    # def test_streamer_collect_list(self,myMonitor,rankStatus):
    #     """
    #     监控中心-数据概览列表接口
    #     :param myMonitor:
    #     :param rankStatus:
    #     :return:
    #     """
    #     url="https://gray.huo1818.com/live-api/v2/streamer/collect-list"
    #     params= {
    #             "avgRewardTopOneNumLast7DaysMax": 0,
    #             "avgRewardTopOneNumLast7DaysMin": 0,
    #             "avgWatchNumLast7DaysMax": 0,
    #             "avgWatchNumLast7DaysMin": 0,
    #             "endDate": "2020-11-11",
    #             "fansNumMax": 0,
    #             "fansNumMin": 0,
    #             "gender": 0,
    #             "myMonitor": myMonitor,
    #             "rankStatus": rankStatus,
    #             "rewardNumMax": 0,
    #             "rewardNumMin": 0,
    #             "startDate": "2020-11-11",
    #             "totalSaleAmountMax": 0,
    #             "totalSaleAmountMin": 0
    #         }
    #     headers={
    #         "gray_df_token": "94dc4e29e52c4548a3e5517714ae2f55175352cb3f7"
    #
    #     }
    #     response=requests.post(url=url,json=params,headers=headers)
    #     code=response.status_code
    #     responseTime=response.elapsed.total_seconds()
    #     print(code)
    #     print(responseTime)
    #     # assert(response.status_code==200)
    # #     pytest.assume(code==200)
    #     pytest.assume(responseTime<1)

    def test_v2_streamer_collect_list(self):
        data_view = DataView()
        r = data_view.v2_streamer_collect_list()
        code = r.status_code
        result_json = json.loads(r.text,strict=False)
        result = result_json["result"]
        success = result_json["success"]
        pytest.assume(code == 200)
        pytest.assume(result != [])
        pytest.assume(success=="true")



    def teardown_class(self):
        print('测试结束')
#
#
# if __name__ == '__main__':
#     pytest.main()





