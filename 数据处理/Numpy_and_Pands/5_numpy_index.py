import numpy as np

A=np.arange(3,15).reshape((3,4))
print(A)



# A[index] 一维数组
# A[index] A[index][index] A[index_line,index_colum] 二维数组
# A[2,:] 第二行的所有的数 A[:,1] 第一列的所有的数
# A[1,1:3] 第一行从第一列到第三列
# for row in A:
	# print(row) 迭代行
# for column in A.T:
	# print(column) 迭代列(使用矩阵反向后再迭代)
# 这一脚本中的flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。
# 而flat是一个迭代器，本身是一个object属性。
# A.flatten()
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

# A.flat 转变成一个只有一行的序列, 
# for item in A.flat: 
# 	print(item)