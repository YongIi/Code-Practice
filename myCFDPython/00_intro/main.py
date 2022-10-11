# 开发人员：leo
# 开发时间：2022/10/7 22:24
# 对文件00_intro的补充

import numpy  # import the array library
import timeit  # timeit模板，使用timeit()函数需要import timeit

a = [1,2,3]
print(a)
print(a+a)  # [1, 2, 3, 1, 2, 3] 列表相加+仅仅是元素的拼接

b=numpy.array(a)  # 转化为数组

print(b,type(b))
print(b+b)  # [2 4 6]  数组的相加+是各个元素的相加

print(b+1)  # [2 3 4]  数组与标量相加，是数组每个元素都与标量相加

print(b**2)  # [1 4 9]

print(numpy.sin(b))  # 正选作用于每一个元素

print("----")

print(range(5))  # 创建一个序列

print(numpy.arange(5))  # [0 1 2 3 4]  创建一个数组

c = numpy.linspace(0,5,11)  # linspace创建一个数组，在开始和结束之间有等距的数字，总共11个等距数字

print(c)
print(len(c))  # 统计个数

print('----')
print(a)
aa = [x+y for x,y in zip(a,a)]
print(aa)

b=numpy.array(a)
bb=b+b
print(bb)

print("---------统计时间-----------")
# timeit(函数名_字符串，运行环境_字符串，number=运行次数)  #使用timeit()函数需要import timeit
# t = timeit('func()', 'from __main__ import func', number=1000)  # 测试一个函数的执行时间
# print(t)

a = range(1000)
time1 = timeit.timeit('aa = [x+y for x,y in zip(a,a)]', 'from __main__ import a', number=20)
print(time1)

b=numpy.array(a)
time2=timeit.timeit('bb = b+b','from __main__ import b', number=20)
print(time2)

print("使用Numpy提升效率倍数：", time1/time2)

