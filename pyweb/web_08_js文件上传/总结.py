#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""验证码
1，数字和字母， OCR 技术
2，极验， python
3，12306， 1， 找开发。
4，人工打码，收费，


1， 鼠标操作。ActionChains
actionchains 用法。  ActionChains(driver).move_to... click().perform()

2, 链式调用：可以在一个方法后面接着调用另外的方法，
返回对象本身。
测试开发：sql, ORM 模型，链式调用

3， 键盘操作。Keys 类。 send_keys(Keys.ENTER)


DOM 对象
节点对应的 HTML 当中的元素构成
document, ===》 HTML 标签， 根节点， root 节点。
标签名对应的就是标签节点
标签当中的属性对应的就是 属性节点。

document.getElementById()


JS 获取元素属性
- e.属性名
- e.getAttribute("属性名")

js 操作：
1， 修改属性
2， 窗口滚动
#js = "window.scrollTo(9000,9000);"  # 实际距离可能没那么大，但在最靠边
# dr.execute_script(js)
3， 管理标签页，打开新窗口。

文件上传：
1， input 元素， e.send_keys()
2, 不是 input, pyautogui.write(),  press()

"""

def move_to():
    print("正在移动")

def click():
    print('点击')

actions = []
actions.append(move_to)
actions.append(click)

for action in actions:
    # action = move_to
    action()
