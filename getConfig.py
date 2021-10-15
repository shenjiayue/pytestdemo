# -*- coding: utf-8 -*-

import  yaml
import  os
# 获取当前文件路径
filePath = os.path.dirname(__file__)
# config的文件路径
path_config=os.path.join(filePath,'config.yaml')

class getConfig:

    def __init__(self):
        with open(path_config, 'r') as f:
            data = f.read()
        self.yaml_reader = yaml.load(data, Loader=yaml.FullLoader)

    def getHOST(self,env='PROD'):
        return self.yaml_reader[env]['HTTP']['HOST']

    def getPORT(self,env='PROD'):
        if self.yaml_reader[env]['HTTP']['PORT']:
            return self.yaml_reader[env]['HTTP']['PORT']
        else:
            return '443'

    def getPATH(self,env='PROD'):
        return self.yaml_reader[env]['HTTP']['PATH']

