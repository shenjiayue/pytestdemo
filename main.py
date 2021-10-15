# -*- coding: utf-8 -*-
'''
Project : pytestdemo
Name : main
Time : 2021/7/11  11:03
Author : shenjiayue

'''
import  yaml
import  os
import requests

from getConfig import getConfig


def send_get(host,path,param,header,port='443'):
    fullpath=host+':'+port+path
    r=requests.get(fullpath,params=param,headers=header)
    print(r.status_code)
    print(r.text)
    return r

def send_post(host,path,data,header,port='443'):
    fullpath = host + ':' + port + path
    r = requests.post(fullpath,headers=header,data=data)
    print(r.status_code)
    print(r.text)
    return r




def readconfig(pathforconfig='config.yaml'):
    # 获取当前文件路径
    filePath = os.path.dirname(__file__)
    # 获取当前文件的realpath
    filerealpath = os.path.realpath(__file__)
    # config的文件路径
    path_config=os.path.join(filePath,pathforconfig)
    with open(path_config,'r') as f:
        data = f.read()
    yaml_reader = yaml.load(data, Loader=yaml.FullLoader)
    print(yaml_reader['uat']['HTTP']['host'])


if __name__ == '__main__':

    a=getConfig().getHOST()
    print(a)
    # https://joinchitchat.com/chitchat-mobile-web/api/v1/fans/follow
    # host='https://joinchitchat.com'
    # path='/chitchat-mobile-web/api/v1/fans/follow'
    # param={'scheduleId':'104274'}
    # header={'cookie':'domain=.joinchitchat.com; path=/; channel=ios-c1000; 1&_device=iPhone&CAAB68CA-1BB4-44CF-8558-F6AB748FE3FA&1.8.9; impl=com.ximalaya.chitchat; 1&_token=335552112&F12FEDF0340C8E4B6E5271BB35A91BBF6C8C2DBCBA418BE05BE563C1CE0CF71B27C460E9A07A2MAA456BF1209692C_; idfa=CAAB68CA-1BB4-44CF-8558-F6AB748FE3FA; device_model=iPhone7Plus; device_name='}
    # # isFollow=1&toUid=6297169
    # data={'isFollow':'1','toUid':'6297169'}
    # # send_get(host,path,param,header)
    # send_post(host,path,data,header)
    # 前n位斐波那契的等差数列的和
    # num = int(input("前n位斐波那契的等差数列的和,输入n"))
    # a=1
    # b=1
    # if num <= 0:
    #     print("error")
    # elif num == 1:
    #     print("1")
    # elif num == 2:
    #     print("2")
    # else:
    #     # sum=前2位的等差数列和
    #     sum=2
    #     n=2
    #
    #     # 求n(#`O′)斐波那契数列的和
    #     while n < num:
    #         # 求斐波那契数列
    #         c=a+b
    #         a=b
    #         b=c
    #
    #         # 针对单个斐波那契c求等差数列的和
    #         i=1
    #         sum_c=0
    #         while i<=c:
    #             sum_c=sum_c+i
    #             i=i+1
    #
    #         # 计算出c的等差数列的和之后，加入到sum中，最终的sum是每个斐波那契数量等差数列的和
    #         sum=sum+sum_c
    #         n=n+1
    #     print(sum)
    #
    #
    #



