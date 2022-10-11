# 开发人员：leo
# 开发时间：2022/10/7 21:08

import numpy  # import the array library
from matplotlib import pyplot  # import plotting library

myArray = numpy.linspace(0,5,10)  # linspace创建一个数组，在开始和结束之间有等距的数字，总共十个数字

print(myArray)

myValues = numpy.array([1,2,3,4,5])

print(myValues, type(myValues))

print(myValues[0],myValues[4])

# 切片将产生新的对象，原对象不发生变化。切片是左闭区间，右开区间
print(myValues[0:3])  # [1 2 3]
print(myValues, type(myValues))

print("--------数组变量的分配--------")

a = numpy.linspace(1,5,5)
print(a,type(a))

b=a  # b和a都是指针，指向了同一个数组，其中一个改变数组，另一个也会改变 assignment by reference
print(b)

a[2]=17
print(a)
print(b)

print("----")

# 如果想要真实地复制一个数组，需要copy()函数
c = a.copy()
print(a)
print(c)
a[4] = 6
print(a)
print(c)