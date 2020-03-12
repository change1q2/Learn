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
   # print('当前日期：',d2)
   # print(d2)

    t1 = int(time.time())
    # print("当前日期时间戳：",t1)
    print(t1)
    return t1
now_datetime()