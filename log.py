# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime
import threading
import getConfig



class Log:
    def __init__(self):
        # 获取当前文件路径
        filePath = getConfig.filePath
        logdirpath=os.path.join(filePath,'logging')
        # 日志文件夹
        if not os.path.exists(logdirpath):
            os.mkdir(logdirpath)
        # 单个日志文件，时间戳命名
        logfilePath = os.path.join(logdirpath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logfilePath):
            os.mkdir(logfilePath)
        # 定义日志
        self.logger=logging.getLogger()
        # 定义日志登记
        self.logger.setLevel(logging.DEBUG)
        # 定义输出文件路径
        handler = logging.FileHandler(os.path.join(logfilePath, "output.log"))
        # 定义终端输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # 日志定义输出路径和格式
        self.logger.addHandler(handler)



