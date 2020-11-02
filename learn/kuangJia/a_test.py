#! /usr/bin/python
# coding=utf-8

import pytest
import yaml

# class TestDemo5():
#     @pytest.mark.parametrize(['a','b'],yaml.safe_load(open("./data.yaml")))
#     def test_data(self,a,b):
#         print(a+b)


def test_success():
    """this test succeeds"""
    assert(1==1)


def test_failure():
    """this test fails"""
    assert(1==2)


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    assert(1==3)