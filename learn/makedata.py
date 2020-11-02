
#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os

def createBigFile():
    for i in range(0,415):
        cmd='mkfile -n 5G /Users/kongzhibing/Desktop/bigFile/'+str(i)+'.jpg'
        os.system(cmd)


def copyFile():
    for i in range(1100,1201):
        cmd='cp /Users/kongzhibing/Desktop/yilian/89621955e24669a5434c7fbb823efc92_67c1f800556ce8713daf0578b693eecc.jpg /Users/kongzhibing/Desktop/1000yilian/'+str(i)+'.jpg'
        os.system(cmd)



copyFile()

