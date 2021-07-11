# -*- coding: utf-8 -*-
'''
Project : pytestdemo
Name : readConfig
Time : 2021/7/11  14:34
Author : shenjiayue

'''
import os
import yaml

realpath=os.path.split(os.path.realpath(__file__))[0]
configpath=os.path.join(realpath,'config.yaml')

# class ReadConfig:
#     def __init__(self):

# if __name__ == '__main__':
#     print(realpath)
#     print(os.path.realpath(__file__))
#     print(configpath)