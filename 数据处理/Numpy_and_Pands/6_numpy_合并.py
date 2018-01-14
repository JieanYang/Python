import numpy as np

A=np.array([1,1,1])[:,np.newaxis]

B=np.array([2,2,2])[:,np.newaxis]

# C=np.vstack((A,B)) # vertical stack
# D=np.hstack((A,B)) # horizontal stack


# 横向数列转化为竖向数列
# A[np.newaxis,:] #行上加了一个维度
# A[:,np.newaxis] #列上加了一个维度

# C=np.concatenate((A,B,B,A),axis=1) # 多个array纵向或横向的合并
print(C)