# -*- coding: utf-8 -*-
# @Time ： 2023/7/18 17:50
# @Auth ： JeremyChim
# @File ：1.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from chardet import detect

a = 'hello, would.\r\rI am Jeremy\r\r'
a = 'cd data\r\r\nls\r\r\nexit\r\r\nsh-3.2# cd data\r\r\nsh-3.2# ls\r\r\ncore      coredump  mdlog     property  thermal   upgrade   wifi\r\r\nsh-3.2# exit\r\r\nexit\r\r\n'
a = a.replace('\r','')
print(str,a)

b = bytes(a, encoding = 'utf-8')
print(bytes,b)

c = str(b, encoding = 'utf-8')
print(str,c)


# print('\thahaha\txixixi')

