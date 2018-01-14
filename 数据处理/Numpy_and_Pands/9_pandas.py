import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
print(s)

dates=pd.date_range('20160101', periods=6)
print(dates)
# 两个效果相同
# print(np.random.random((6,4)))
# print(np.random.randn(6,4))
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

df1=pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

# 必须传入index进去,即一个数组
df2=pd.DataFrame({'A':1.,'B':pd.Timestamp('20130102'),'C':[2,5,2,5]})
print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe()) # 忽略日期和字符串，适用于于数字运算
print(df2.T)
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_values(by='C'))