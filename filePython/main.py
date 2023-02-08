# 创建和打开文件

"""
1、打开文件
2、写入内容，读取内容
3、关闭文件，仅读取文件时不需要关闭文件，可以靠python自动回收垃圾

语法：
file = open(filename[,mode, buffering])
file是文件对象
mode是打开模式，r是只读，w只写，a是追加，b是以二进制文件处理，各模式可以用+链接
w，a都可以在没有该文件时创建文件，但r不行
buffering是缓存，0是不缓存，1是缓存，>1是缓冲区大小

"""

file = open("status.txt", 'a')