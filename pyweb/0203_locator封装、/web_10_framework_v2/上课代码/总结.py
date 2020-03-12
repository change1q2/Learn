#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
driver.get()   # 访问网站
driver.find_element...() 找元素
driver.find_element_by_xpath()   # 不要去 copy 网站给我们提供的 xpath 表达式。
绝对路径

# 找到元素以后
e = driver.find_element_by_xpath()
e 类型是什么类型？？ WebElement 对象
# 获取 id, e.id
# e.text 获取文本
# 获取指定的属性 e.get_attribute('href')

# 操作元素
e.click() 点击元素
e.send_keys()   发送数据
e.submit()    提交表单（e 要在 form 表单当中。）


# 等待
1， 强制等待，
使用场景： 1， 隐式等待，显式等待不适合的。  系统交互，多个系统衔接的地方。
 e.g.  :  js 指令发送的时候，   2， 文件上传，pyautogui, pywin32

2, 隐式等待
使用场景，初始化浏览器以后，直接添加. (一个浏览器会话对象只需要添加一次)
只适合用来等待查找元素。   窗口切换等场景隐式等待不行

3， 显式等待
使用场景： 窗口切换， iframe, alert, (visible, precence, click)
小技巧：先不适用显示等待，看隐式等待能不能找到，如果不能找到，再用显示等待。


# 窗口切换， 封装好方法。 window ， 依据：window_handler 窗口句柄
driver.switch_to.window()
等待

iframe,  依据： index, name， webelement 对象。
等待： 4， （By.ID, 'id_value'）

alert,


鼠标操作：ActionChains()
ac = ActionChains()
ac.move_to().click().drag_and_drop().
ac.perform()


键盘操作：
e.send_keys(Keys.Enter)

POM  PO 模式   Page Object Model
页面对象模型

讲测试逻辑和页面逻辑分离，把页面相关的操作都放到一个页面类当中。
在测试的时候，直接调用相关页面的操作方法， 实现了页面操作的复用性。
1， 复用性
2， 可维护性，
3， 扩展性，有新的页面，建立一个新的页面类就
4， 可读性。



出现几秒就不见的弹框定位：主要是用 js 实现：
浏览器 f12 sources ,暂停定位

分层：
1， 测试逻辑；
2， 页面逻辑；
3， 数据管理；  分组，分组的依据：页面逻辑是否一致。

4， locator 元素定位方式分层。  （By.ID, "id_value"）

"""