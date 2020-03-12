#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽


driver = Chrome()
driver.get("file:///D:/subjects/python_test/resources/20181217/test.html")

f = driver.find_element_by_name('myfile')

f.click()
# 一定要注意等待
time.sleep(2)


def send_file(file):

    diag = win32gui.FindWindow("#32770","打开")
    print(diag)

    ex32 = win32gui.FindWindowEx(diag,0,'ComboBoxEx32',None)
    print(ex32)
    box = win32gui.FindWindowEx(ex32,0,'ComboBox',None)
    print(ex32)
    editor  = win32gui.FindWindowEx(box,0,'Edit',None)
    print(editor)
    subm = win32gui.FindWindowEx(diag,0,'Button','打开(&O)')
    time.sleep(2)
    print(win32gui.SendMessage(editor, win32con.WM_SETTEXT, 0, file))
    time.sleep(2)
    print(win32gui.SendMessage(diag, win32con.WM_COMMAND, 1, subm))