import pytest
import  pytest_assume
import yaml

from zhibozhushou.common.common import Common
from zhibozhushou.testcase.testcasebase import Testcasebase



class Test_sellApi(Testcasebase):
    token = {'token': Testcasebase().getToken()}

    # @pytest.mark.parametrize('casedata',[{'activityGoodsId': 3425,'sellCountNum': 1500,'sellCountIncr': 100}])
    @pytest.mark.parametrize('casedata', yaml.safe_load(open("./data/data_test_sell_count.yaml")))
    def test_sell_count(self, casedata):
        """
        修改自动给直播间的商品修改销量
        :param casedata:
        :return:
        """
        self.casedata=casedata
        self.data = casedata.update(self.token)
        self.data = Common().template("./zhibozhushouApi/test-sell-count.yaml", self.casedata)
        self.getResponse(self.data)
        assert (self.r.status_code == 200)