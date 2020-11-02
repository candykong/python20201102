#! /usr/bin/python
# coding=utf-8

from HTMLTestRunner_PY3 import HTMLTestRunner

import unittest

class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownClass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_Case01(self):
        print("testcase01")
        self.assertEqual(1,1,msg='判断相等')

    @unittest.skipIf(1+1==2,"跳过")
    def test_Case02(self):
        print("testcase01")
        self.assertAlmostEqual(1, 1, msg='判断相等')

    @unittest.skip
    def test_Case03(self):
        print("testcase01")
        self.assertEqual(1, 1, msg='判断相等')

class demo1(unittest.TestCase):
    def test_demo1_Case01(self):
        print("testcase01")
        self.assertEqual(1, 1, msg='判断相等')


    def test_demo1_Case01(self):
        print("testcase01")

class demo2(unittest.TestCase):
    def test_demo2_Case01(self):
        print("testcase01")
        self.assertEqual(1, 1, msg='判断相等')


    def test_demo2_Case01(self):
        print("testcase01")




if __name__ == '__main__':
    #unittest.main()  //执行所有的用例

    """使用testSuit执行不同类中的方法"""""
    # suit=unittest.TestSuite()
    # suit.addTest(demo("test_Case01"))
    # suit.addTest(demo("test_demo1_Case01"))
    # unittest.TextTestRunner().run(suit)

    """使用TestLoader().load执行不同的类"""
    # suite=unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suitall=unittest.TestSuite(suite,suite1)
    # unittest.TextTestRunner().run(suitall)

    """unittest.defaultTestLoader.discover加载某路径下的所有用例去执行"""
    # test_dir="/Users/kongzhibing/PycharmProjects/locust/"
    # discover=unittest.defaultTestLoader.discover(test_dir,"unittestTest.py")

    """使用HTMLTestRunner运行测试用例生成报告"""
    report_title='用例执行报告'
    desc='用于展示修改样式后的HTMLTestRunner'
    report_file='unittestTest.html'

    testsuite=unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo))
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(demo1.test_demo1_Case01()))

    with open(report_file,'wb') as report:
        runner = HTMLTestRunner(stream=report,title=report_title,description=desc)
        runner.run(testsuite)




