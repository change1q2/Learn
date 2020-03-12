'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''

import datetime
import time


def now_datetime():
    now=datetime.datetime.now()
    d2 = datetime.datetime.strptime(now.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    return d2

def now_datetime_time():
    t1 = int(time.time())
    return t1


# now_datetime()
#now_datetime_time()