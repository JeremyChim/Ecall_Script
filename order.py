# -*- coding: utf-8 -*-
# @Time ： 2023/7/17 17:35
# @Auth ： JeremyChim
# @File ：order.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import os
import subprocess
import chardet

# result = os.popen('adb devices').read()
# print(result)

cmds = [
    "cd data",
    "ls",
    "exit",#这是是非常关键的，退出
]
obj = subprocess.Popen("adb shell", shell= True, stdin=subprocess.PIPE, stderr=subprocess.PIPE) # stdout=subprocess.PIPE,, stderr=subprocess.PIPE
info, error = obj.communicate(("\n".join(cmds) + "\n").encode('utf-8'))

# info = bytes(info, encoding='ascii')
# ret = chardet.detect(info)
# print(ret)

# info = str(info, encoding="ascii")
# info = info.replace('\r','')
# for item in info:
#     if item:
#         print(item)
#
# info = str(info, encoding='ascii')
print(info)
print(error)