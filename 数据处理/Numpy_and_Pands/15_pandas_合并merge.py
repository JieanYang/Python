import pandas as pd
import numpy as np

# 依据一组key合并
# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                              'A': ['A0', 'A1', 'A2', 'A3'],
#                              'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                               'C': ['C0', 'C1', 'C2', 'C3'],
#                               'D': ['D0', 'D1', 'D2', 'D3']})



# res=pd.merge(left,right,on='key')

# 依据两组key合并
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                       'key2': ['K0', 'K1', 'K0', 'K1'],
#                       'A': ['A0', 'A1', 'A2', 'A3'],
#                       'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                        'key2': ['K0', 'K0', 'K0', 'K0'],
#                        'C': ['C0', 'C1', 'C2', 'C3'],
#                        'D': ['D0', 'D1', 'D2', 'D3']})


# 合并时有4种方法 how = ['left', 'right', 'outer', 'inner']，预设值how='inner'。
# res=pd.merge(left,right,on=['key1','key2'],how='outer')

# Indicator 显示合并是怎样合并的
# indicator=True会将合并的记录放在新的一列。
# df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
# df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})

# 依据col1进行合并，并启用indicator=True，最后打印出
# res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)

# 自定indicator column的名称，并打印出
# res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')


# 依据index合并
# left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
#                      'B': ['B0', 'B1', 'B2']},
#                      index=['K0', 'K1', 'K2'])
# right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
#                       'D': ['D0', 'D2', 'D3']},
#                      index=['K0', 'K2', 'K3'])


#依据左右资料集的index进行合并，how='outer',并打印出
# res = pd.merge(left, right, left_index=True, right_index=True, how='outer')

#依据左右资料集的index进行合并，how='inner',并打印出
# res = pd.merge(left, right, left_index=True, right_index=True, how='inner')


# 解决overlapping的问题
# boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
# girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

#使用suffixes解决overlapping的问题
# res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')


# pandas 里还有一个 join功能，同merge相同，只是表达形式不同 