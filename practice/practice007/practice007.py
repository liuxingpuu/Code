# -*- coding:utf-8 -*-
'''
斐波那契数列
Created on 2016年10月27日
@author: liuxingpuu
'''
def fib(n):
    if n == 0:
        return 1
    if n ==1:
        return 2
    else:
       return(fib(n-1) + fib(n-2))


# 获取用户输入
nterms = int(input("您要输出几项? "))

# 检查输入的数字是否正确
if nterms <= 0:
   print("输入正数")
else:
   print("斐波那契数列:")
   for i in range(nterms):
       print(fib(i))