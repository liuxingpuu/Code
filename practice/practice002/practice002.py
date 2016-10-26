#coding=utf-8
'''
Generating a random code 
By @liuxingpuu
'''
import random

def couponCode(length):
    s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.sample(s,length))
l=input("Enter the length of the random code: ")
i=1
while i<=200:
    print couponCode(int(l))
    i=i+1
    