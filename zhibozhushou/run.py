
import pytest
import os
import sys

if __name__ == '__main__':
    # print(os.path.dirname(sys.path[0]))
    sys.path.append(os.path.dirname(sys.path[0]))
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # rootPath = os.path.split(curPath)[0]
    # sys.path.append(rootPath)
    # apitest=SellApi()
    # apitest.test_sell_count()
    pytest.main(['-q','./testcase/test_sellApi.py'])