#!/usr/bin/python
# -*- coding:UTF-8 -*-

import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

'''
sender='328721121@qq.com'
authCode='ppwrpjgpgcmocbcj'
passwd='KZB800312kzb'
receiver=['kzb18575503902@163.com','2544114868@qq.com']
'''


#不带附件
def sendMail1(sender,authCode,receiver):
    try:
        msg=MIMEText('邮件发送...')
        msg['From']=formataddr(["发件人昵称",sender])
        msg['to']=formataddr(["收件人昵称",receiver])
        msg['Subject']='邮件主题-发送测试报告'

        #邮件正文内容
        msg.attach(MIMEText('接口自动化测试结束，发送邮件。。。'))

        server=smtplib.SMTP_SSL('smtp.qq.com',465)
        server.login(sender,authCode)
        server.sendmail(sender,receiver,msg.as_string())
        server.quit()
        print('邮件发送成功')
    except Exception as e:
        print(e.args)




#带附件
def sendMail(sender,authCode,receiver,filename):
    try:
        msg=MIMEMultipart()
        msg['From']=formataddr(["发件人昵称",sender])
        #msg['to']=formataddr(["收件人昵称",receiver])
        #多人邮件必须使用join
        msg['to']=Header(",".join(receiver))
        msg['Subject']='邮件主题-发送测试报告'

        #邮件正文内容
        msg.attach(MIMEText('接口自动化测试结束，发送邮件。。。'))

        #构造附件
        att1=MIMEText(open(filename,'rb').read(),'base64','utf-8')
        att1["Content-Type"]='application/octet-stream'
        att1["Content-Disposition"]='attachment; filename="testreport.html"'
        msg.attach(att1)


        server=smtplib.SMTP_SSL('smtp.qq.com',465)
        server.login(sender,authCode)
        server.sendmail(sender,receiver,msg.as_string())
        server.quit()
        print('邮件发送成功')

    except Exception as e:
        print(e.args)


#sendMail1()
#sendMail(sender,authCode,receiver,'/Users/kongzhibing/PycharmProjects/auto/test_report/autoReport_2019-12-0216:25:54.html')
