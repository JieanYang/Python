import numpy as np
a=np.random.random((2,4))
print(a)
b=a*10
print(b)
print(np.sum(b))
print(np.min(b))
print(np.max(b))

# + - * /
# 平方 c=b**2
# np.sin(),np.cos(),np.tan()
# 矩阵乘法 np.dot(), np.arange().dot()
# np.random.random((2,4))
# np.sum(a, axis=0)  表示在列中求和
# np.min(a,axis=1)  表示在行中返回最小数值
# np.max()