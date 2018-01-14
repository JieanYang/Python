import pandas as pd
import numpy as np

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,columns=['A','B','C','D'])
print(df)

# 选择列
# print(df['A'],'\n',df.A)
# 选择index,行
# print(df[0:3],'\n',df['20130102':'20130104'])

# select by label:loc 
# print(df.loc['20130102'])
# print(df.loc[:,['A','B']])
# print(df.loc['20130102',['A','B']]) # 以标签名字来查找索引而不是数字

# select by position: iloc
# print(df.iloc[3])
# print(df.iloc[3,1])
# print(df.iloc[3:5,1:3])
# print(df.iloc[[1,3,5],1:3])

# 综合loc 和 iloc
# mixed selection: ix
# print(df.ix[:3,['A','C']])

# Boolean indexing
# print(df[df.A > 8])