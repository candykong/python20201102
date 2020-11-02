#!/usr/bin/python
# -*- coding:UTF-8 -*-

import json


#json转换为字典
def jsonToDic(json1):
    result = json.loads(json1,strict=False)
    return result


#字典转换为json
def dicToJson(dic):
    result=json.dumps(dic,indent=2,sort_keys=True)
    return result