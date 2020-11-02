#! /usr/bin/python
# coding=utf-8
import logging
from time import sleep, ctime



def loop0():
    logging.info("start loop0 at"+ctime())
    sleep(4)

if __name__=='__main__':
   loop0()
