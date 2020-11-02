#!/usr/bin/python
# -*- coding：UTF-8 -*-

#import numpy as np
#import pandas as pd

import os

import pymysql.cursors

'''
import getConfig

#数据库连接基本信息
host=getConfig.host
port=getConfig.port
user=getConfig.user
passwd=getConfig.passwd

'''


host='rm-bp1pj9n34wv8431j1.mysql.rds.aliyuncs.com'
port=3306
user='zhiyi_ldl'
passwd='Zhiyiliandanlu123456'


'''
def dbConnection(sql):
    db = pymysql.connect(
        host='rm-bp1pj9n34wv8431j1.mysql.rds.aliyuncs.com',
        port=3306,
        user="zhiyi_ldl",
        passwd="Zhiyiliandanlu123456",
        charset='utf8')

    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data
'''


def dbConnection(sql):
    db = pymysql.connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        charset='utf8')

    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data



    








