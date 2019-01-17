# -*- coding: utf-8 -*-
# Quick python script explanation for programmers
import os                     #导入模块

def main():                   #函式名
    print ("Hello world")  #python最好也最个性的语法：使用缩进代替语句块声明

    print ("这是Alice\'的问候.")
    print ('这是Bob\'的问候')

    foo(5,10)

    print ('=' * 10)
    print ('这将直接执行'+os.getcwd())

    counter =  0
    counter += 1

    food = ['apple','banana','pear','mengo']
    for i in food:
        print ('I realy like integer:'+i)

    print ('count to 10')
    for i in range(10):
        print (i)

def foo(param1, secondParam):
    res = param1+secondParam
    print ('%s plus %s equals to %s'%(param1, secondParam, res))
    if res < 50:
        print ('this one')
    elif (res>=50)and((param1==42)or(secondParam==24)):
        print ('that one')
    else:
        print ('en...')
    return res
    '''多行注释的内容不用遵守当前缩进格式，只要开始的三撇缩进格式正确即可'''

    if _name_=='_main_':
        main()

