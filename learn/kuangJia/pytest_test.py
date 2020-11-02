#! /usr/bin/python
# coding=utf-8
# noinspection PyUnresolvedReferences
import pytest
import yaml



def setup_module():
    print("模块开始")

def teardown_module():
    print("模块结束")


class TestDemo1():
    def setup_class(self):
        print("")

    def teardown_class(self):
        print("")


    def inc(self,x):
        self.x=x
        return self.x + 1


    def test_demo1_1(self):
        print("111")
        # assert self.inc(3) == 5
        pytest.assume(1==1)
        pytest.assume(2==2)


class TestDemo2():
    def inc(self,x):
        self.x=x
        return self.x + 1

    def test_dem02_1(self):
        print("111")
        assert self.inc(4) == 5

class TestDemo3():
    def test_demo3_1(self,login):
        print("1，登陆")
        pass

    def test_demo3_2(self):
        print("2，不需要登陆")
        pass

    def test_demo3_3(self,login):
        print("3，需要登陆")
        pass


@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("执行teardown")
    print("关闭浏览器")

def test_search1(open):
    print('test_search1')
    raise NameError
    pass

class TestDemo4():
    # @pytest.mark.parametrize("test_input","expected",["1+2",8],["1+2",4],["1+2",3])
    # def test_eval(self,test_input,expected):
    #     assert eval(test_input)==expected

    #参数组合
    @pytest.mark.parametrize("x",[1,2])
    @pytest.mark.parametrize("y",[3,4,5])
    def test_foo(self,x,y):
        print(f"测试参数组合x:{x},y:{y}")


class TestDemo5():
    @pytest.mark.parametrize(['a','b'],yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a+b)



"""在cmd命令中执行'pytest [-参数] 文件名[::l类名][::类方法]    #[表示可选]'"""
#
# if __name__ == '__main__':
#     # pytest.main()
#     # pytest.main('-v -x TestDemo1')
#     pytest.main([' --html=report.html --self-contained-html,TestDemo2'])
