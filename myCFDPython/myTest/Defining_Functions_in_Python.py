# 开发人员：leo
# 开发时间：2022/10/27 11:10

# Defining Functions in Python

def simpleadd(a, b):
    return a+b

print(simpleadd(3,4))

"""
a, b = 0, 1
print(a, b)
a, b = b + 3, a + b  # 并行赋值。b+3的值赋值给a，a+b的值算出来后传给b。同时进行，不分先后
print(a, b)
"""

def fibonacci(n):  # 计算斐波那契数列中的第n个数并返回
    a, b = 0, 1
    for i  in range(n):
        a, b = b, a + b
    return a

for n in range(10):
    print(fibonacci(n))


