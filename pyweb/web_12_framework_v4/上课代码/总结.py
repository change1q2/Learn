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





提升测试效率的前提：
1， 保证测试用例运行的稳定性。
2， 用例之间要独立，不能相互影响。


注意事项：
1， 清空输入框数据
2， 对测试用例排序，有副作用的排在后面


复杂的测试用例： 投标
前置条件
1， 登录
2， 有标可以投。 如果没有标，创建，并且审核。
3， 有钱。  没有钱就要充值，冲多少？大于投资金额。
4， 标的有余额可以供你投。

前置条件一定要用 web 自动化操作去实现吗？？
1， 能用接口的手段直接满足条件；
2， 能不能直接修改数据库？ pymysql , 操作数据库
3， 手工实现吗？

前置条件只是一个条件而已，和你的测试主要逻辑



TODO:   在有页面跳转的情况下，一定要确保新页面打开再定位元素，
否则找到的是上一个页面的元素。
解决方法：
等待

# 如何断言投资成功
1， sql, 一般是在接口测试当中，校验数据使用。
2， web 测试，ui, 测试的是： 界面的显示是否正确。
投标成功界面会如何显示： 预期结果是什么？
1， 查找页面当中是否有“投标成功！”的元素，如果存在，测试通过，find_element_by_xpath(//文本)
2， 定位元素，对比 text 文本



多个类用到的共用方法和属性  ==== 》 继承

basepage 基页，

"""