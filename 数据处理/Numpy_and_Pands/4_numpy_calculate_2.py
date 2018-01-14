import numpy as np

A=np.arange(19,7,-1).reshape((3,4))
print(A)
print(np.sort(A))

# 计算最小值的索引 np.argmin(A)
# 计算最大值的索引 np.argmax(A)
# 计算平均值 np.mean(A), np.arange().mean(), np.average(A)
# 计算中位数 np.median(A)
# 累加 np.cumsum(A)
# 累差 np.diff(A)
# 非零的数 np.nonzero(A) -> 返回两个array，前一个是行数，后一个表示列数
# 排序 np.sort(A) 逐行排序
# 矩阵的反向 np.transpose(A)， A.T
# 截断 np.clip(a, a_min, a_max, out=None) 大于max都是a_max，小于min都是a_min
# 指定行与列 axis