#coding=utf-8
'''
find words and count
By @liuxingpuu
'''
import re

fin= open("example","r")
fout = open("reuslt.txt","w")
str=fin.read()
reObj = re.compile("\b?([a-zA-Z]+)\b?")
words = reObj.findall(str)
word_dict={}
for word in words:
    if(word_dict.has_key(word)):
        word_dict[word.lower()]=max(word_dict[word.lower()],words.count(word.lower())+words.count(word.upper())+words.count(word))
    else:
        word_dict[word.lower()]=max(0,words.count(word.lower())+words.count(word.upper())+words.count(word))
for(word,number) in word_dict.items():
    fout.write(word+":%d\n"%number)