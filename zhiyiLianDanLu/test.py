from zhiyiLianDanLu.multiApi.jianKongCenter import dataView


import pytest
import os
import sys

from zhiyiLianDanLu.multiApi.userInfo import UserInfo

if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))
    # dataView=dataView.DataView()
    # dataView.v2_streamer_collect_list()
    pytest.main(['-q','./testcase/test_jianKongCenter/test_dataView.py'])
