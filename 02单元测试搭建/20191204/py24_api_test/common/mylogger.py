"""
============================
Author:柠檬班-木森
Time:2019/11/25
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os
import logging
from common.myconfig import conf
from common.contants import LOG_DIR


# 读取配置文件中的数据
level = conf.get_str("logging", "level")
f_level = conf.get_str("logging", "f_level")
s_level = conf.get_str("logging", "s_level")
filename = conf.get_str("logging", "filename")
# 获取日志文件的绝对路径
file_path = os.path.join(LOG_DIR,filename)


class MyLogger(object):

    @staticmethod
    def create_logger():
        # 一、创建一个名为：python24的日志收集器
        my_log = logging.getLogger("python24")
        # 二、设置日志收集器的等级
        my_log.setLevel(level)
        # 三、添加输出渠道（输出到控制台）
        # 1、创建一个输出到控制台的输出渠道
        sh = logging.StreamHandler()
        # 2、设置输出等级
        sh.setLevel(s_level)
        # 3、将输出渠道绑定到日志收集器上
        my_log.addHandler(sh)
        # 四、添加输出渠道（输出到文件）
        fh = logging.FileHandler(file_path, encoding="utf8")
        fh.setLevel(f_level)
        my_log.addHandler(fh)
        # 五、设置日志输出的格式
        # 创建一个日志输出格式
        formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
        # 将输出格式和输出渠道进行绑定
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        return my_log


# 调用类的静态方法，创建一个日志收集器
my_log = MyLogger.create_logger()
