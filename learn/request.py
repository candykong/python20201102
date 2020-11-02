#!/usr/bin/python
# -*- coding:UTF-8 -*-


import requests

from learn.common import excelOperation
import getConfig
import json
import ast
from responseConvert import getStatus



#获取运行环境
envHost=getConfig.envHost

#获取团队中主账号的登陆token和userId1
token=getConfig.token
userId1=getConfig.userId1

#获取团队中另外一个成员的userid2
userId2=getConfig.userId2



class Collector:
    def __init__(self,envHost):
        self.envHost=envHost

    def getResponse(self,url,method,form,params,headers):
        if method=='get' and params=='':
            response=requests.get(url=self.envHost+url,headers=headers)
        elif method=='get' and params!='':
            response=requests.get(url=self.envHost+url,params=json.loads(params),headers=headers)
        elif method=='post' and form=='json':
            response=requests.post(url=self.envHost+url,json=json.loads(params),headers=headers)
        else:
            response=requests.post(url=self.envHost+url,files=ast.literal_eval(params),headers=headers)
        return response


#实例话
collector=Collector(envHost)
path='/Users/kongzhibing/Desktop/炼丹炉测试/接口用例.xlsx'
sheet='监控台'
#各参数对应得列
urlColumn = excelOperation.getColumn(path, sheet, 'url')
methodColumn = excelOperation.getColumn(path, sheet, 'method')
formColumn = excelOperation.getColumn(path, sheet, 'form')
paramsColumn = excelOperation.getColumn(path, sheet, 'params')
codeColumn = excelOperation.getColumn(path, sheet, 'params')

statusColumn = excelOperation.getColumn(path, sheet, 'status')
codeColumn = excelOperation.getColumn(path, sheet, 'code')
msgColumn = excelOperation.getColumn(path, sheet, 'responseMsg')
errorColumn = excelOperation.getColumn(path, sheet, 'responseError')


def goRun():
    rowsCount = excelOperation.getTotalRows(path, sheet)
    for i in range(2,rowsCount):
        try:
            url = excelOperation.outputExcel(path, sheet, i, urlColumn)
            method = excelOperation.outputExcel(path, sheet, 7, methodColumn)
            form = excelOperation.outputExcel(path, sheet, 7, formColumn)
            params = excelOperation.outputExcel(path, sheet, 7, paramsColumn)
            headers = {
                'gray_df_token': token
            }
            response = collector.getResponse(url, method, form, params, headers)
            code = response.status_code
            status = getStatus.getSuccess(response.text)
            responseMsg = response.text
            excelOperation.inputExcel(path, sheet, i, codeColumn, code)
            excelOperation.inputExcel(path, sheet, i, statusColumn, status)
            excelOperation.inputExcel(path, sheet, i, msgColumn, responseMsg)

        except Exception as msg:
            excelOperation.inputExcel(path, sheet, i, errorColumn, msg)






'''
url = common.outputExcel(path,sheet,7,4)
method = common.outputExcel(path,sheet,7,5)
form = common.outputExcel(path,sheet,7,6)
params = common.outputExcel(path,sheet,7,7)
headers = {
            'gray_df_token': token
        }
response=collector.getResponse(url,method,form,params,headers)
print(response.text)
'''



