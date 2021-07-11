# -*- coding: utf-8 -*-
'''
Project : pytestdemo
Name : main
Time : 2021/7/11  11:03
Author : shenjiayue

'''
import  yaml




def readconfig():
    f = open('config.yaml')
    data = f.read()
    yaml_reader = yaml.load(data)
    print(yaml_reader['uat']['HTTP']['host'])

if __name__ == '__main__':
    readconfig()

    print ("2233")
