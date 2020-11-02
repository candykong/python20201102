#!/usr/bin/python
# -*- coding：UTF-8 -*-

#import numpy as np
#import pandas as pd
from learn.DBselect import dbConnect

#查询主播的基本信息
def SelectStreamerInfo():
    sql="select  `kwai_id`,`eid`,`user_name`,`gender`,`horoscope`,`city`,`fans_num`,`product_num`,`oss_avatar_url`,`brief`,`has_kwai_shop`,`tag` " \
    "from `ai_ks_live`.`ks_user`" \
    " where `streamer_id`=188888880"
    result = dbConnect.dbConnection(sql)
    dict = {}
    dict['kwai_id']=result[0]
    dict['eid']=result[1]
    dict['user_name']=result[2]
    dict['gender']=result[3]
    dict['horoscope']=result[4]
    dict['city']=result[5]
    dict['fans_num']=result[6]
    dict['product_num']=result[7]
    dict['oss_avatar_url']=result[8]
    dict['brief']=result[9]
    dict['has_kwai_shop']=result[10]
    dict['tag']=result[11]
    return dict

SelectStreamerInfo()








