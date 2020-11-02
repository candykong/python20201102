#! /usr/bin/python
# coding=utf-8

import pytest

@pytest.fixture()
def login():
    print("需要登陆")