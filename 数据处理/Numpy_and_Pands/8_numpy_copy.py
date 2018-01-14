import numpy as np

a=np.arange(4)

# =的赋值方式会带有关联性
# b=a
# c=a
# d=b
# a[0]=11 # [11 1 2 3]
# 改变a,b,c,d任何一个都会影响到其他变量的值

# copy() 的赋值方式没有关联性
# b=a.copy() # deep copy
# a[0]=11
# print(a)
# print(b)
