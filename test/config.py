# -*- coding: utf-8 -*-
# @Time ： 2023/7/16 2:15
# @Auth ： JeremyChim
# @File ：4.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

from configparser import ConfigParser

cf = ConfigParser()
cf.read('config.ini', encoding='utf-8')

print(cf.sections())
print(cf.options(section='birthday'))
print(cf.items(section='birthday'))

print(cf.get(section='name',option='jer'))
print(cf.get(section='birthday',option='jer'))
# cf.add_section(section='age')
# cf.set(section='age',option='jer',value='28')
# cf.set(section='age',option='mav',value='24')
# cf.set(section='age',option='bro',value='31')

# f = open('4.ini','w')
# cf.write(f)