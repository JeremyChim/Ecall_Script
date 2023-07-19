# -*- coding: utf-8 -*-
# @Time ： 2023/7/16 2:37
# @Auth ： JeremyChim
# @File ：3.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import os
from time import sleep
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from configparser import ConfigParser
from datetime import datetime

w = ttk.Window()

l = ttk.Label(w)
l.pack(fill=X, expand=YES, padx=10, pady=10)

t = ttk.Text(l, height=25)
t.pack(fill=X, expand=YES)

# bar = ttk.Scrollbar(t, command=t.yview, style='primary',orient="vertical")
# bar.pack(side=RIGHT, fill=X)

# t.config(yscrollcommand=bar.set)

def fun(order):
    time = str(datetime.now())[:-4]
    text = time + ' >>> ' + order + '\n'
    t.insert(index='end', chars=text)

    r = os.popen(order).read()
    if r == '':
        r = 'error: no devices/emulators found'

    time = str(datetime.now())[:-4]
    text = time + ' <<< ' + r + '\n'
    t.insert(index='end', chars=text)

cf = ConfigParser()
cf.read('order.ini', encoding='utf-8')

se = '指令'
op = cf.options(se)

for i in op:
    val = cf.get(se, i)
    b = ttk.Button(l, text=i, command=lambda x=val:fun(x))
    b.pack(side=LEFT, fill=X, expand=YES, padx=(0,1))

w.mainloop()