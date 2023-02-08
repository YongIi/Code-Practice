# 开发人员：leo
# 开发时间：2022/12/12 17:36

# 读写npy文件

"""
numpy.save(file, arr, allow_pickle=True, fix_imports=True)

file:文件名/文件路径
arr:要存储的数组
allow_pickle:布尔值,允许使用Python pickles保存对象数组(可选参数,默认即可)
fix_imports:为了方便Pyhton2中读取Python3保存的数据(可选参数,默认即可)
"""

import numpy as np
a=np.array(range(20)).reshape((2,2,5))
print(a)

filename='a.npy'     #保存路径
# 写文件
np.save(filename,a)

#读文件
b=np.load(filename)
print(b)
print(b.shape)
